import React from 'react'
import { useState, useEffect } from 'react'

function Product() {
    const [count, setCount] = useState(1)
    const increase = (value) =>{
        setCount([...count,count+value])
    console.log(count)
    }
  return (
    <div>
        <button onClick={()=>{increase(1)}}>+</button>
        <p>{count}</p>
    </div>
  )
}

export default Product