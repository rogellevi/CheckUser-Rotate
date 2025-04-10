import http.server
import urllib.request

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        try:
          
            target_host = 'us1.chadvps.xyz'
            target_port = 5555 #
            url = 'http://' + target_host + ':' + str(target_port) + self.path

          
            content_length = int(self.headers['Content-Length'])

           
            post_data = self.rfile.read(content_length)

         
            req = urllib.request.Request(url, data=post_data, headers=self.headers, method='POST')
            response = urllib.request.urlopen(req)

        
            data = response.read()

        
            self.send_response(response.getcode())
            for header, value in response.headers.items():
                self.send_header(header, value)
            self.end_headers()

          
            self.wfile.write(data)

        except Exception as e:
            # Em caso de erro, retorna uma resposta com status 500
            self.send_error(500, str(e))

if __name__ == '__main__':
    # Endereço e porta do servidor proxy
    proxy_host = '0.0.0.0' #AQUI NÂO MECHE
    proxy_port = 5757  #NOVA PORTA

    # Inicia o servidor proxy
    proxy_server = http.server.HTTPServer((proxy_host, proxy_port), ProxyHandler)
    print('Proxy iniciado na porta', proxy_port)

    # Inicia o servidor proxy
    try:
        proxy_server.serve_forever()
    except KeyboardInterrupt:
        pass

    # Encerra o servidor proxy
    proxy_server.server_close()
    print('Proxy encerrado.')
