var url = "http://localhost/8000";

function log(message) {
    //Send a htpp request obvs not really
    console.log(message)
}

//This is saying that a METHOD called 'log' is being added to an 'exports' attribute of the module object 
//And setting it to the log function defined above.
module.exports.log = log;  //The .log part could be replaced with anything could be       module.exports.foshijd = log;

//The same thing for variables can be done.

module.exports.testNameItsNotReallyGlobal = url;
//Note that the exported name could be called anything. so it could instead be 
//     module.exports.endPoint = url;