import React,{useState} from 'react'
import "./Mood.css"
import logo from "../../assets/logo-blue.png";
import profile from "../../assets/profile.png";

export default function Sleep() {

    const [sleepHours,setSleepHours]=useState(5);
    const [sleepQuality, setSleepQuality]=useState("");
    const [sleepFeel, setFeel]=useState("");



    return (
    <div className='h-screen'>
        <div className='fixed w-full flex justify-between items-center px-20 h-24' >
            <img src={logo} alt="" className=''/>
            <button className="w-auto h-12 p-3 rounded-full bg-custombluebutton"><img src={profile} alt='' className="h-full"></img></button>
        </div>
        <div className="flex flex-col justify-end items-center h-screen">
            <div className="flex flex-col h-5/6 w-3/4 rounded-t-3xl shadow-md justify-center items-center">
                <div className="text-3xl m-14 font-bold">SLEEP TRACKER</div>

                <div className="text-xl mt-14 mb-8">How are you feeling today?</div>
                <div className='flex mt-0'>
                    <button className="w-36 h-12 mx-4 rounded-sm bg-red text-white font-bold" onClick={()=>{setSleepQuality("AWFUL")}}>AWFUL</button>
                    <button className="w-36 h-12 mx-4 rounded-sm bg-yellow text-white font-bold" onClick={()=>{setSleepQuality("BAD")}}>BAD</button>
                    <button className="w-36 h-12 mx-4 rounded-sm bg-green text-white font-bold" onClick={()=>{setSleepQuality("MEH")}}>MEH</button>
                    <button className="w-36 h-12 mx-4 rounded-sm bg-yellow text-white font-bold" onClick={()=>{setSleepQuality("BAD")}}>BAD</button>
                    <button className="w-36 h-12 mx-4 rounded-sm bg-green text-white font-bold" onClick={()=>{setSleepQuality("MEH")}}>MEH</button>
                </div>
                
                <div className="text-xl m-14">How would you rate your stress levels? </div>
                <input type='range' min='0' max='10' defaultValue={sleepHours} className='slider' onChange={(e)=>{setSleepHours(e.target.value)}}></input>
                <div className='text-xl mt-8'>{sleepHours}</div>

                <div className="text-xl mt-14 mb-8">How would you rate your quality of sleep?</div>
                <div className='flex mt-0'>
                    <button className="w-48 h-12 mx-4 rounded-sm bg-bluelight text-white font-bold" onClick={()=>{setFeel("AWAKE")}}>WIDE AWAKE </button>
                    <button className="w-48 h-12 mx-4 rounded-sm bg-bluemed text-white font-bold" onClick={()=>{setFeel("TIRED")}}>A BIT TIRED</button>
                    <button className="w-48 h-12 mx-4 rounded-sm bg-bluedark text-white font-bold" onClick={()=>{setFeel("SLEEPY")}}>SLEEPY</button>
                </div>

                <button className="w-36 h-12 mt-24 rounded-full bg-black text-white font-bold" onClick={()=>{
                    if(sleepFeel!=="" && sleepQuality!==""){
                        
                    }
                }}>SUBMIT</button>

            </div>
        </div>
    </div>
  )
}
