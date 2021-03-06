import http.client
import json
import socketserver
import socket
import utilities as u
import http.server
import termcolor
from utilities import Seq
from urllib.parse import parse_qs, urlparse

ARGUMENT = "?content-type=application/json"
SERVER = 'rest.ensembl.org'
PORT = 8080
IP = "127.0.0.1"

socketserver.TCPServer.allow_reuse_address = True

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

id_dict = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
           "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000226906",
           "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
           "ANK2": "ENSG00000145362"}


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Message to send back to the clinet
        try:
            url = urlparse(self.path)
            path = url.path
            arguments = parse_qs(url.query)
            print(path)
            ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ls.bind((IP, PORT))
            ls.listen()




            if self.path == "/":
                contents = u.read_html_file("index.html").render()
            elif path == "/listSpecies":
                dict_answer = u.make_ensmbl_request("/info/species", ARGUMENT)  # + "&" + "species=homo_sapiens"
                list_species = dict_answer["species"]
                length_list = []
                for d in list_species:
                    length = d["common_name"]
                    length_list.append(length)
                length = len(length_list)

                try:
                    if 0 <= int(arguments["limit"][0]) <= length:
                        n_species = int(arguments["limit"][0])  # check what happens if input empty !!!

                        list_species = list_species[0:n_species]
                        name_list = []
                        for d in list_species:
                            v = d["common_name"]
                            name_list.append(v)
                        content_dict = {"length": length, "species": name_list, "limit": n_species}

                        contents = u.read_html_file("listSpecies.html").render(
                                context=content_dict)
                    else:
                        contents = u.read_html_file("error.html").render(
                            context={"error": "Please enter an integer number between 0 and "+ str(length)})
                except KeyError:
                    contents = u.read_html_file("error.html").render(context={"error":"Please enter an integer number"})



            elif path == "/karyotype":
                try:
                    specie = arguments["karyotype"][0]  # check what happens if input empty !!!
                    dict_answer = u.make_ensmbl_request("info/assembly/" + specie,
                                                        ARGUMENT)  # + "&" + "species=homo_sapiens"
                    karyotypes = dict_answer["karyotype"]
                    content_dict = {"specie":specie, "karyotypes": karyotypes}
                    contents = u.read_html_file("karyotype.html").render(context=content_dict)
                except KeyError:
                    contents = u.read_html_file("error.html").render(context={"error":"Please enter a valid species"})

            elif path == "/chromosomeLength":
                try:
                    specie = arguments["specie"][0].replace(" ", "_")

                    n_chromosome = arguments["length"][0].upper()  # check what happens if input empty !!!
                    dict_answer = u.make_ensmbl_request("info/assembly/" + specie,
                                                        ARGUMENT)
                    try:
                        for d in dict_answer["top_level_region"]:
                            for k, v in d.items():
                                if k == "name" and v == str(n_chromosome):
                                    length = d["length"]
                                else:
                                    pass
                        content_dict = {"length": length, "chromosome": n_chromosome, "specie": specie}
                        contents = u.read_html_file("chromosomeLength.html").render(context=content_dict)
                    except UnboundLocalError:
                        contents = u.read_html_file("error.html").render(
                            context={"error": "Please enter a valid chromosome"})
                except KeyError:
                    contents = u.read_html_file("error.html").render(
                        context={"error": "Please enter valid data"})
            elif path == "/gene":
                try:
                    gene = arguments["gene"][0]
                    gene_id = id_dict[gene]
                    dict_answer = u.make_ensmbl_request("/sequence/id/" + gene_id, ARGUMENT)
                    geneseq = dict_answer["seq"]
                    geneinfo = dict_answer["desc"].split(":")
                    genestart = int(geneinfo[3])
                    genend = int(geneinfo[4])
                    genelength = genend - genestart
                    geneid = geneinfo[2]
                    chromosome_name = geneinfo[1]
                    sequence = Seq(geneseq)
                    base_perc, total_length = Seq.base_perc(sequence.count_base_dict())
                    content_dict= {"gene": gene, "geneseq": geneseq, "genestart": genestart,
                                 "genend": genend, "genelength": genelength, "geneid": geneid,
                                 "chromosome_name": chromosome_name, "total_length": total_length,
                                 "base_perc": base_perc}
                    contents = u.read_html_file("gene.html").render(
                        context=content_dict)
                except KeyError:
                    contents = u.read_html_file("error.html").render(
                        context={"error": "Please enter a valid gene"})

            elif path == "/chromosome":
                try:
                    chromosome = arguments["chromosome"][0]
                    start = int(arguments["start"][0])
                    end = int(arguments["end"][0])
                    if 0 <= start < end:
                        dict_answer = u.make_ensmbl_request(
                            "/phenotype/region/homo_sapiens/" + chromosome + ":" + str(start) + "-" + str(end), ARGUMENT)

                        genes_list = []
                        if dict_answer == []:
                            genes_list.append("There are no genes in that region")
                            content_dict = {"chromosome": chromosome, "start": start, "end": end
                                , "genes_list": genes_list}
                            contents = u.read_html_file("chromosome.html").render(
                                context=content_dict)

                        else:
                            try:
                                if type(dict_answer) is dict:
                                    check = dict_answer["error"]
                                else:
                                    check =  dict_answer[0]["error"]

                                contents = u.read_html_file("error.html").render(
                                    context={"error": "Please enter valid chromosome."})
                            except KeyError:
                                for d in dict_answer:
                                    dictionary = d["phenotype_associations"]
                                    try:
                                        for i in dictionary:
                                            genes_list.append(i["attributes"]["associated_gene"])
                                    except KeyError:
                                        pass
                                if genes_list == []:
                                    genes_list.append("There are no genes in that region")
                                content_dict= {"chromosome": chromosome, "start": start, "end": end
                                        , "genes_list": genes_list}
                                contents = u.read_html_file("chromosome.html").render(
                                    context=content_dict)

                    else:
                        contents = u.read_html_file("error.html").render(
                            context={"error": "Please enter valid integer numbers. Start must be smaller than end and both must be positive"})
                except KeyError:
                    contents = u.read_html_file("error.html").render(
                        context={"error": "Please enter valid data"})
                except ValueError:
                    contents = u.read_html_file("error.html").render(
                        context={"error": "Please enter valid integer numbers."})

            else:
                contents = u.read_html_file("error.html").render(context={
                    "error": "Sorry, the information you entered is not available in ensmlb"})

            # Generating the response message
            self.send_response(200)  # -- Status line: OK!

            # Define the content-type header:

            try:
                trying = arguments["json"][0]
                contents = content_dict
                contents = json.dumps(contents)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(contents.encode()))
            except KeyError:
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(contents.encode()))
            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(contents.encode())
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
