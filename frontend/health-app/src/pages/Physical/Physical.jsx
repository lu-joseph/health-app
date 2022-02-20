import React,{useState} from 'react'
import "./Physical.css"
import logo from "../../assets/logo-blue.png";
import profile from "../../assets/profile.png";
import axios from 'axios';

export default function Sleep() {

    const [water,setWater]=useState(5);
    const [exercise, setExercise]=useState(5);



    return (
    <div className='h-screen'>
        <div className='fixed w-full flex justify-between items-center px-20 h-24' >
            <a href="/dashboard"><img src={logo} alt="" className=''/> </a>
            <button className="w-auto h-12 p-3 rounded-full bg-custombluebutton"><img src={profile} alt='' className="h-full"></img></button>
        </div>
        <div className="flex flex-col justify-end items-center h-screen">
            <div className="flex flex-col h-5/6 w-3/4 rounded-t-3xl shadow-md justify-center items-center">
                <div className="text-3xl m-14 font-bold">PHYSICAL HEALTH TRACKER</div>
                
                <div className="text-xl m-14">How many glasses of water did you drink? </div>
                <input type='range' min='0' max='10' defaultValue={water} className='slider' onChange={(e)=>{setWater(e.target.value)}}></input>
                <div className='text-xl mt-8'>{water}</div>

                <div className="text-xl m-14">How many hours of exercise did you get? </div>
                <input type='range' min='0' max='10' defaultValue={exercise} className='slider' onChange={(e)=>{setExercise(e.target.value)}}></input>
                <div className='text-xl mt-8'>{exercise}</div>
                <a href='/dashboard'>
                <button className="w-36 h-12 mt-24 rounded-full bg-black text-white font-bold" onClick={()=>{
                    var bodyFormData = new FormData();
                    bodyFormData.append('hours', exercise);
                    bodyFormData.append('userid', 1);
                    bodyFormData.append('date', "2022-02-20");
                    axios({
                        method: "post",
                        url: "http://localhost:5000/api/activity/addEntry",
                        data: bodyFormData
                    })
                        .then(response => {console.log(response)})
                        .catch(error => {console.log(error)})
                    var bodyFormData2 = new FormData();
                    bodyFormData2.append('cups', water);
                    bodyFormData2.append('userid', 1);
                    bodyFormData2.append('date', "2022-02-20");
                    axios({
                        method: "post",
                        url: "http://localhost:5000/api/water/addEntry",
                        data: bodyFormData2
                    })
                        .then(response => {console.log(response)})
                        .catch(error => {console.log(error)})
                    
                }}>SUBMIT</button></a>

            </div>
        </div>
    </div>
  )
}
