##Ricardo Jimenez Todd##

This directory includes 

* `node.py`: which
  * defines a node class. 
    * contains a name, list of children, and a count that's initially zero
    * implements a `show(graph)` method recursively prints the nodes within graph  
  * An `increment(graph)` method that increments the counts of all nodes within graph. 
* `localDemo.py`: which creates a dag of nodes, which it prints, increments, and prints again.

Your tasks are
* to create 
  * a jsonrpc server that exports the `increment(graph)` function
  * a client that demonstrates the effect of `increment()` being remotely executed on the graph from localDemo.py.
  * a file named `request.json` containing a the manually genrated contents of jsonrpc request to `increment()`
   equivalent to the one produced by your client.   You should use nc to confirm that it's correct.

*`localDemo.py`: contains the functions to transform a python object to a JSON
*object and viceversa.

*`node.py`: contains the basic structure of a tree node.

*`jserver.py`: listens on a certain port and recieves a tree encoded as a JSON
 object. Decodes it and increments 1 to every node, then re encodes it to a
 JSON object and sends it back.

*`jclient.py`: builds a small tree and encodes it as a JSON object, connects
 to a server on a certain port and sends the JSON object.
