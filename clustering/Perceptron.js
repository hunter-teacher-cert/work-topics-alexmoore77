/*

Note:  I reviewed several additional online support materials to comprehend this difficult topic.

*/

class Perceptron {
  
  ////////////////////////
  //  Percepton constructor() 
  ////////////////////////
  /*
  Percepton has an instance variable of weights[]
  These are a series of random numbers between -1 and 1.
  So each Percepton has n * random weights as instance variables...
  Each Percepton also has a learningRate of 0.01
*/
  // parameter is number of inputs
  constructor(n){
  // initialize an array of weights here
    this.weights = []
    // should have same amount of weights as inputs
    // weights should be random values between -1 and 1
    for(let i = 0; i < n; i++) {
      this.weights.push(random(-1, 1))
    }//for
    // don't worry about this until writing training function
     this.learningRate = 0.01; 
  }//constructor
  
  
  ////////////////////////
  //  activate()
  ////////////////////////
  // determine if sum of calculated weights and inputs is higher or lower than zero
  // return 1 if greater than zero
  // return -1 if less than zero
  activate(sum){
    if(sum > 0){
      return 1;
    } else {
      return -1
    }//else
  }//activate
  
   ////////////////////////
  //  feedForward()
  ////////////////////////
  
  //feedForward algorithm
  // 1. multiply each input by its corresponding weight
  // 2. sum all the weighted inputs
  // 3. pass sum through activation function
  feedForward(inputs){
  let sum = 0
  for(let i = 0; i < inputs.length; i++) {
    sum += this.weights[i]*inputs[i]
  }//for
    return this.activate(sum);
  }//feedForward
  
  // finish training function for homework
  train(inputs, desired){
    // store result of feed forward here
 let guess=this.feedForward(inputs);
    
    // error is difference between desired result and guess
  let error = desired - guess;
    
    // adjust all weights by adding learning rate times error times inputs
    // weight1 + learningRate*error*input1 
    // -> do same for all weights
   
     
  for(let i = 0; i < this.weights.length; i++) {
      this.weights[i] = this.weights[i]+this.learningRate*error*inputs[i] ; 
  
  }//for
 
  }//train
  
}//perceptron