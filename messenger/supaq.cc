#include <zmq.h>
#include <string>
#include <cassert>
#include <cstring>

#include "supaq.hpp"

std::map<std::string, int> TOPICS = {{"topic1", 5000}, {"topic2", 5002}};

/*
getCompleteAddress build the tcp string to pass into Zeromq.
The topic passed in must be a declared topic in the TOPICS map. 
*/
std::string getCompleteAddress(std::string topic, bool isSubcriber) {
    int port = TOPICS[topic];
    std::string fullAddress;
    if (isSubcriber) {
        fullAddress = "tcp://localhost:";
    } else {
        fullAddress = "tcp://*:";
    }
    fullAddress += std::to_string(port);
    printf("%s\n", fullAddress.c_str());
    return (fullAddress.c_str());
}

/*Publisher Functions*/

void Publisher::connect(std::string inpTopic) {
    std:: string address = getCompleteAddress(inpTopic, false);
    //zmq::context_t context();
    context = zmq_ctx_new();
    socket = zmq_socket(context, ZMQ_PUB);
    int rc = zmq_bind(socket, address.c_str());
    assert(rc == 0);
    topic = inpTopic;
};

void Publisher::publish(std::string msg) {
    int msgLen = msg.length();
    char buffer[msgLen];
    std::strcpy(buffer, msg.c_str());
    printf("%s\n", buffer);
    int rc = zmq_send(socket, buffer, msgLen+1, 0);
    assert(rc != -1);
};

/* Subscriber Functions*/

void Subscriber::connect(std::string topicSet) {
    std::string address = getCompleteAddress(topicSet, true);
    topic = topicSet;
    context = zmq_ctx_new();
    socket = zmq_socket(context, ZMQ_SUB);
    zmq_connect(socket, address.c_str());
    zmq_setsockopt(socket, ZMQ_SUBSCRIBE, "", 0);
};

void Subscriber::recieve() {
    char buf [256];
    int rc = zmq_recv (socket, buf, 256, 0);
    assert (rc != -1);
    printf("From %s: %s\n",topic.c_str(), buf);
}