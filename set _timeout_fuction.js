let number =0;
const limit =10;
const intervalid = setinterval(() => {
    console.log(number);
    number++;

if (number > limit){
    clearinterval(intervalid);
    console.log("reached the limit. stopping tho increment.");
    }
},1000);

