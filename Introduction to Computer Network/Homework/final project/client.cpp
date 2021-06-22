#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <netinet/in.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<iostream>
#include<string.h>
using namespace std;
void Server_Request_Procedure(int sockfd, struct sockaddr* serv_addr){
	int flag = 1;
	int status;
	char buffer[256];
	string greeting = "What's your requirement? 1.DNS 2.QUERY 3.QUIT:";
	while(flag){
		cout << greeting;
		int requirement;
		cin >> requirement;
		if (requirement == 1){
		/* Now ask for a message from the user, this message
    	 * will be read by server
   		*/
			printf("Input URL address: ");
			char addr[20];
			scanf("%s", addr);
   			bzero(buffer,256);
   			fgets(buffer,255,stdin);
   
   			/* Send message to the server */
   			int n = write(sockfd, buffer, strlen(buffer));
  			if (n < 0) {
				perror("ERROR writing to socket");
				exit(1);
			}
			/* Now read server response */
			bzero(buffer,256);
			n = read(sockfd, buffer, 255);
			if (n < 0) {
				perror("ERROR reading from socket");
				exit(1);
			}
			printf("%s\n",buffer);

		}else if(requirement == 2){
			string id;
			cout << "Input your student ID :";
			cin >> id;

		}else if(requirement == 3){
			flag = 0;

		}else{
			flag = 0;
		}
	}
	status = write (sockfd, "Hello!", strlen("Hello")+1);
}
int main(){
	struct sockaddr_in server_addr;	
	int sockfd;	
	/*Initialize the socket structure*/
	server_addr.sin_family = PF_INET;	
	server_addr.sin_port = htons(5000);	
	server_addr.sin_addr.s_addr = inet_addr ("127.0.0.1");	
	//connect to the server	
	sockfd = socket (PF_INET, SOCK_STREAM, 0);
	if (sockfd < 0){
		perror("Error opening socket");
		exit(1);
	}	
	/* Now connect to the server */
	if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
      perror("ERROR connecting");
      exit(1);
   }
	/* server request procedure */
	Server_Request_Procedure(sockfd, (struct sockaddr*)&server_addr);

	close(sockfd);	
	
	return 0;
}