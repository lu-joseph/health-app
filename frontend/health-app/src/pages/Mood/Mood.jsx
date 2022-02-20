import React,{useState} from 'react'
import "./Mood.css"
import logo from "../../assets/logo-blue.png";
import profile from "../../assets/profile.png";
import axios from 'axios';

export default function Sleep() {

    const [stress,setStress]=useState(5);
    const [mood, setMood]=useState("");
    const [events, setEvents]=useState("");



    return (
    <div className='h-screen'>
        <div className='fixed w-full flex justify-between items-center px-20 h-24' >
            <img src={logo} alt="" className=''/>
            <button className="w-auto h-12 p-3 rounded-full bg-custombluebutton"><img src={profile} alt='' className="h-full"></img></button>
        </div>
        <div className="flex flex-col justify-end items-center h-screen">
            <div className="flex flex-col h-5/6 w-3/4 rounded-t-3xl shadow-md justify-center items-center">
                <div className="text-3xl m-14 font-bold">MOOD TRACKER</div>

                <div className="text-xl mt-14 mb-8">How are you feeling today?</div>
                <div className='flex mt-0'>
                    <button className={"w-36 h-12 mx-4 rounded-sm text-white font-bold"+ (mood==="AWFUL"?" bg-gray":" bg-red")} onClick={()=>{setMood("AWFUL")}}>AWFUL</button>
                    <button className={"w-36 h-12 mx-4 rounded-sm text-white font-bold"+ (mood==="BAD"?" bg-gray":" bg-peach")} onClick={()=>{setMood("BAD")}}>BAD</button>
                    <button className={"w-36 h-12 mx-4 rounded-sm text-white font-bold"+ (mood==="MEH"?" bg-gray":" bg-bluemed")} onClick={()=>{setMood("MEH")}}>MEH</button>
                    <button className={"w-36 h-12 mx-4 rounded-sm text-white font-bold"+ (mood==="GOOD"?" bg-gray":" bg-green")} onClick={()=>{setMood("GOOD")}}>GOOD</button>
                    <button className={"w-36 h-12 mx-4 rounded-sm text-white font-bold"+ (mood==="GREAT"?" bg-gray":" bg-blueish")} onClick={()=>{setMood("GREAT")}}>GREAT</button>
                </div>
                
                <div className="text-xl m-14">How would you rate your stress levels? </div>
                <input type='range' min='0' max='10' defaultValue={stress} className='slider' onChange={(e)=>{setStress(e.target.value)}}></input>
                <div className='text-xl mt-8'>{stress}</div>


                <div className="text-xl m-14"> List some events that might have contributed to stress: </div>
                <textarea className='rounded-lg border-black border-2' value={events} onChange={(e)=>{setEvents(e.target.value)}} cols="40" rows="4"></textarea>

                <button className={"w-36 h-12 mt-24 rounded-full text-white font-bold" + (mood!==""?' bg-black':' bg-gray cursor-default')} onClick={()=>{
                    if(mood!==""){
                        
                    }
                }}>SUBMIT</button>

            </div>
        </div>
    </div>
  )
}
