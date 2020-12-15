# ZMQ_Examples
various basic usages of ZMQ framwork，more about ZMQ(https://zeromq.org/).
### 多生产者单消费者-python示例
在该示例中，生产者为server，其会使用python多线程的方式并发地向本地消息队列中发送数据；
消费者为client，其会逐条读取生产者产生的数据，运行时，分别运行两个程序即可，注：如果先
运行server，可能client会丢失第一条产生的数据，建议先运行client，再运行server
