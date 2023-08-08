//assign all elements
const demoId = document.getElementById('demo');
const demoClass = document.getElementsByClassName('demo');
const demoTag = document.getElementsByTagName('article');
const demoQuery = document.querySelector('#demo-query');
const demoQueryAll = document.querySelectorAll('demo-query-all');

//Change the border of id demo to purple
demoId.style.border = "3px dotted purple";

//Change border of class demo to orange
for (i = 0; i < demoClass.length; i++) {
    demoClass[i].style.border = '2px solid orange';
}

for (i = 0; i < demoTag.length; i++) {
    demoTag[i].style.border = '2px solid green';
}

