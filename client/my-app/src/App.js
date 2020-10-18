import React, { useEffect } from 'react';
import './App.css';
import styled from 'styled-components'

const Disc = styled.div`
      background-color: ${props => props.color};
      height: ${props => props.size}px;
      width: ${props => props.size}px;
      margin: ${props => props.margin}px;
      z-index: ${props => props.zindex};
`

function App() {

  
  
  var step =[[[3, 2, 1], [], []], [[3, 2], [], [1]], [[3], [2], [1]], [[3], [2, 1], []], [[], [2, 1], [3]], [[1], [2], [3]], [[1], [], [3, 2]], [[], [], [3, 2, 1]]]
  
  var updateTowers = (step_) => {
    let towerA = step_[0]
    let towerB = step_[1]
    let towerC = step_[2]
    window.setTimeout(() => {
      for(let i = 0; i < towerA.length; i += 1)
      {
        var elem1 = document.getElementById("disc-"+towerA[i]);
        elem1.style.left = 10 + 'px'
        elem1.style.transform ="rotate(0deg)"
      }
      
      for(let i = 0; i < towerB.length; i += 1)
      {
        var elem2 = document.getElementById("disc-"+towerB[i]);
        elem2.style.left = 130 + 'px'
        elem2.style.transform = "rotate(360deg)"
   
      }
      
      for(let i = 0; i < towerC.length; i += 1)
      {
        var elem3 = document.getElementById("disc-"+towerC[i]);
        elem3.style.left = 235 + "px"
        
        elem3.style.transform = "rotate(720deg)"
      }
   
    },1000)
  }
var count  = 0
 const counter = () =>
      {
        
        count++;
        if(count < step.length){
            updateTowers(step[count])
        }
       
        setTimeout(counter, 1000);
      }
  React.useEffect(() => {
    counter()
  },[])
  

  return (
   <div>
        <div class="anim">
          <Disc id="disc-3" zindex={0} size={70} margin={10} color={"#070d59"}></Disc>
          <Disc id="disc-2" zindex={1} size={60} margin={15} color={"#ee6f57"}></Disc>
          <Disc id="disc-1" zindex={2} size={50} margin={20} color={"#8d93ab"}></Disc>
        </div>
   </div>
  );
}

export default App;
