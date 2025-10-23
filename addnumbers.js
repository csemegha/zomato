function addNumbers(){
    var nums=[];
    for(var n=0;n<arguments.length;n++){
        nums[n]=arguments[n];
    }
    var sum=0;
    for(var i=0;i<nums.length;i++){
        sum+=nums[i];
    }
    console.log("sum of numbers="+sum);
}
addNumbers(1,2,3,4);
addNumbers(10,20,30,40);