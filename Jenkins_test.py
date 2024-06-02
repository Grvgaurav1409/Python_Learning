import jenkins

server = jenkins.Jenkins('http://jenkins:8080', username='Gaurav', password='Grv@123')
user = server.get_whoami()
node = server.get_node_info('Grv_Jenkins')
server.enable_node('Grv_Jenkins')
print(node)