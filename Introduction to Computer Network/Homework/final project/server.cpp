#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>
#include <netinet/in.h>
#include <string.h>
#include <iostream>
using namespace std;
int main( int argc, char *argv[] ) {
   struct sockaddr_in my_addr;
   struct sockaddr_in client_addr;
   int sockfd, streamfd, port, status, n;
   socklen_t addr_size;
   char buffer[256];
   port = 5000;
   bzero(&my_addr, sizeof(my_addr));
   my_addr.sin_family = PF_INET;
   my_addr.sin_port = htons(port); 
   my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
   sockfd = socket(PF_INET, SOCK_STREAM, 0);
   bind(sockfd, (struct sockaddr*)&my_addr, sizeof(struct sockaddr_in));
   listen(sockfd, 10);
   addr_size = sizeof(client_addr);
   cout << "Server is running...\n";
   while(1){
      streamfd = accept(sockfd, (struct sockaddr *)&client_addr, &addr_size);
      cout << "New request...\n";
      n = read(streamfd, buffer, 255);
      if (n < 0) {
            perror("ERROR reading from socket");
            exit(1);
      }
      cout << "Reading request...\n";
      cout << "From client: " << buffer;
      bzero(buffer,256);
      int n = write(streamfd, buffer, strlen(buffer));
      if (n < 0) {
            perror("ERROR writing to socket");
            exit(1);
      }
      close(streamfd);
   }
   return 0;
}

