#include <bits/stdc++.h>

#define n 100  //max no of topics
using namespace std;

class Subscriber;


class master
{
    private:
    Subscriber* sub[n][5];
    int no_of_sub[n];

    public:
    master()
    {
        for(int i=0; i < n; i++)
            no_of_sub[i] = 0;
    }

    void pub(int topic, string msg);

    void addSubscriber(int topic, Subscriber* subobj)
    {
        sub[topic][no_of_sub[topic]] = subobj;
        no_of_sub[topic]++;
    }

};


class Publisher
{
    private:
    int topic;
    master* m;

    public:
    Publisher(int t, master* mas)
    {
        topic = t;
        m = mas;
    }
    void publish(string msg)
    {
        m->pub(topic, msg);
    }


};


class Subscriber
{
    private:
    string s;
    master* m;

    public:
    Subscriber(int topic, master* mas)
    {
        m = mas;
        m->addSubscriber(topic, this);
    }
    void callback(string msg)
    {
        s = msg;
    }
    string get()
    {
        return s;
    }
};

void master::pub(int topic, string msg)
{
    for(int i=0; i < no_of_sub[topic]; i++)
    {
        sub[topic][i]->callback(msg);
    }
}


int main()
{
    master m;
    Subscriber s(1, &m);
    Publisher t(1, &m);
    t.publish("Welcome");
    cout<<s.get();

    return 0;
}