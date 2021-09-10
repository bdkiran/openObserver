#include <iostream>
#include <string>
#include <thread>
#include <unistd.h>

#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

#include "supaq.hpp"

void publishering(std::string topic) {
    std::cout << "Starting publisher!!!" << std::endl;
    Publisher pub;
    pub.connect(topic);
    int i = 0;
    std::string messageToSend;
    while(true) {
        messageToSend = "Message: " + std::to_string(i);
        pub.publish(messageToSend);
        i++;
        sleep(1);
    }
};

void subscribing(std::string topic) {
    std::cout << "Starting subscriber!!!" << std::endl;
    Subscriber sub;
    sub.connect(topic);
    while(true) {
        sub.recieve();
    }
};

// void getSocket() {
//     int sockfd;
//     struct sockaddr_in serv_addr;

//     sockfd = socket(AF_INET, SOCK_STREAM, 0);

//     bzero((char *) &serv_addr, sizeof(serv_addr));

//     serv_addr.sin_family = AF_INET;
//     serv_addr.sin_addr.s_addr = INADDR_ANY;
//     serv_addr.sin_port = 0;

//     if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0){
//         perror("failed to bind");
//         //std::cout << "failed to bind with errno: "<< errno << std::endl;
//         exit(1);
//     }

//     socklen_t len = sizeof(serv_addr);
//     if (getsockname(sockfd, (struct sockaddr *)&serv_addr, &len) < 0){
//         perror("failed to get hostname");
//         exit(1);
//     }
//     printf("Local port : %u\n", serv_addr.sin_port);
//     close(sockfd);
// }

int main()
{
    std::cout << "Starting the program!!!" << std::endl;
    std::thread th2(subscribing, "topic1");
    std::thread th1(publishering, "topic1");
    std::thread th3(subscribing, "topic2");
    std::thread th4(publishering, "topic2");
    th2.join();
    th1.join();
    
    return 0;
}
