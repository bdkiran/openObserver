#include <zmq.h>
#include <string>
#include <map>

class Publisher {
    private:
        void *context = NULL;
        void *socket = NULL;
        void *port = NULL;
    public: 
        std::string topic;
        void connect(std::string inpTopic);
        void publish(std::string msg);
};

class Subscriber {
    private:
        void *context = NULL;
        void *socket = NULL;
        void *port = NULL;
    public:
        std::string topic;
        void connect(std::string topicSet);
        void recieve();
};
