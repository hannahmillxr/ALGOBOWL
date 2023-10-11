We have some python files that perform different functions 

"python run_output.py input.txt output.txt" runs our current code on input.txt
and outputs our result to output.txt (according to the format specified for algobowl) 

"python verify.py input.txt output.txt" tests if the graph in output.txt is a valid result for the given
graph from input.txt. 

"python generate_input.py n m input.txt" will generate a random connected graph with up to n nodes and m edges
The resulting graph will be stored in input.txt 

"python run_random_kruskals.py -i n input.txt output.txt" runs our current code on input.txt
and outputs our result to output.txt (according to the format specified for algobowl). Runs n times each time it slightly
perturbs the input to get an optimal outcome. 

"python visualize.py < input.txt" visualizes graph from input. Writes graphviz file to stdout. 

"python see.py input.txt output.txt" visualizes map of output graph on input graph. Writes graphviz file to stdout. 


These files are a little slow because of the networkx import. However, thats why the jupyter notebook is nice. 
