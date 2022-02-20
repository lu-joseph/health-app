import React,{useEffect, useState} from 'react'
import settings from "../../assets/settings.png";
import exit from "../../assets/exit.png";
import logo from "../../assets/logo-blue.png";
import profile from "../../assets/profile.png";
import sleep from "../../assets/sleep.png"
import journal from "../../assets/journal.png"
import nutrition from "../../assets/nutrition.png"
import mood from "../../assets/mood.png"
import dashboard from "../../assets/dashboard.png";
import { Doughnut } from 'react-chartjs-2';
import plus from "../../assets/plus.png";
import axios from 'axios'

export default function Dashboard() {
  const [score,setScore]=useState(0);
  const [firstname, setFirstname]=useState("");
  const [sleepHoursToday, setSleepHoursToday]=useState(0);
  const [recommendedSleepHours, setRecommendedSleepHours]=useState(0);
  const [activeHoursToday, setActiveHoursToday]=useState(0);
  const [recommendedActiveHours, setRecommendedActiveHours]=useState(0);
  const [waterIntakeToday, setWaterIntakeToday]=useState(0);
  const [recommendedWaterIntake, setRecommendedWaterIntake]=useState(0);

  useEffect(()=>{
    fetch("http://localhost:5000/api/dashboard/getScore/1", {method: 'GET'})
     .then(response => response.json())
     .then(data => {setScore(data)})
     .catch(error => {console.log(error)});
    
    fetch("http://localhost:5000/api/userdata/1", {method: 'GET'})
     .then(response => response.json())
     .then(data => {setFirstname(data["firstname"])})
     .catch(error => {console.log(error)});
    
    fetch("http://localhost:5000/api/sleep/feedback/1", {method: 'GET'})
    .then(response => response.json())
    .then(data => {setRecommendedSleepHours(data["recommended_hours"]);
                    if (data["entryFound"]) setSleepHoursToday(data["hours"]);})
    .catch(error => console.log(error));

    fetch("http://localhost:5000/api/activity/feedback/1", {method: 'GET'})
    .then(response => response.json())
    .then(data => {setRecommendedActiveHours(data["recommended_hours"]); 
                    if (data["entryFound"]) setActiveHoursToday(data["hours"]);})
    .catch(error => console.log(error));

    fetch("http://localhost:5000/api/water/feedback/1", {method: 'GET'})
    .then(response => response.json())
    .then(data => {setRecommendedWaterIntake(data["recommended_intake"]);
                    if (data["entryFound"]) setWaterIntakeToday(data["cups"]);})
    .catch(error => console.log(error));
  },[]
  );

  return (
    <div className='h-screen'>
      <div className='fixed w-full flex justify-between items-center px-20 h-24' >
          <img src={logo} alt="" className=''/>
          <button className="w-auto h-12 p-3 rounded-full bg-custombluebutton"><img src={profile} alt='' className="h-full"></img></button>
      </div>
      <div className='flex w-screen'>
        <div className='w-96 h-screen pt-32 flex flex-col items-center'>
          <div className="h-24 w-full flex justify-start items-center border-8 border-white hover:border-l-gray">
            <img src={dashboard} alt='' className='pl-20'></img>
            <div className={'text-md pl-3 text-bluemed'}>Dashboard</div>
          </div>
          <div className="h-24 w-full pl-32 flex justify-start items-center border-8 border-white hover:border-l-gray">
            <a href='/form/sleep'><div className={'text-md text-gray'}>Sleep</div></a>
          </div>
          <div className="h-24 w-full pl-32 flex justify-start items-center border-8 border-white hover:border-l-gray">
            <a href=''><div className={'text-md text-gray'}>Nutrition</div></a>
          </div>
          <div className="h-24 w-full pl-32 flex justify-start items-center border-8 border-white hover:border-l-gray">
            <a href='/form/mood'><div className={'text-md text-gray'}>Mood</div></a>
          </div>
          <div className="h-24 w-full pl-32 flex justify-start items-center border-8 border-white hover:border-l-gray">
            <a href=''><div className={'text-md text-gray'}>Journal</div></a>
          </div>
          <div className="h-24 w-full mt-auto flex justify-start items-center border-8 border-white hover:border-l-gray">
            <img src={settings} alt='' className='pl-20'></img>
            <div className={'text-md pl-3 text-gray'}>Settings</div>
          </div>
          <div className="h-24 w-full flex justify-start items-center border-8 border-white hover:border-l-gray">
            <img src={exit} alt='' className='pl-20'></img>
            <div className={'text-md pl-3 text-gray'}>Log Out</div>
          </div>
        </div>
        <div className='w-full h-screen px-5% pb-20 pt-32 grid grid-cols-4 gap-1 grid-rows-dash'>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-3 col-start-1 flex flex-col justify-center items-center justify-self-center self-center'>
            <div className="text-3xl m-4 text-gray font-bold">Score</div> 
            <div className="text-9xl m-4 font-bold">{score}</div>
            <div className="text-3xl m-4 text-gray font-bold">out of 100</div> 
          </div>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-3 col-start-1 flex flex-col justify-center items-center justify-self-center self-center'>
          </div>
          <div className="row-start text-5xl ml-10 self-center font-montserrat">Hello {firstname}</div>
          <div className="row-start-2 text-lg ml-10 text-gray">Today</div>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-5 col-start-1 flex flex-col justify-center items-center justify-self-center self-center'>
            <img src={sleep} alt='' className="object-contain m-5"/>
            <div className="text-3xl m-5 font-bold">SLEEP</div>
            <a href='/form/sleep'>
              <button className="w-40 h-12 m-5 border-bluemed border-4 rounded-full bg-white text-bluemed font-bold">UPDATE <img className='mx-2 h-3 inline' src={plus} alt=''/></button>
              </a>
          </div>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-5 col-start-2 flex flex-col justify-center items-center justify-self-center self-center'>
            <img src={nutrition} alt='' className="object-contain m-4"/>
            <div className="text-3xl m-4 font-bold">NUTRITION</div>
            <button className="w-40 h-12 m-4 border-bluemed border-4 rounded-full bg-white text-bluemed font-bold">UPDATE <img className='mx-2 h-3 inline' src={plus} alt=''/></button>
          </div>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-5 col-start-3 flex flex-col justify-center items-center justify-self-center self-center'>
            <img src={mood} alt='' className="object-contain mt-2 mb-3"/>
            <div className="text-3xl m-4 font-bold">MOOD</div>
            <a href='/form/mood'>
              <button className="w-40 h-12 m-4 border-bluemed border-4 rounded-full bg-white text-bluemed font-bold">UPDATE <img className='mx-2 h-3 inline' src={plus} alt=''/></button>
              </a>
          </div>
          <div className='rounded-xl mb-4 w-72 shadow-md h-72 row-start-5 col-start-4 flex flex-col justify-center items-center justify-self-center self-center'>
            <img src={journal} alt='' className="object-contain m-4"/>
            <div className="text-3xl m-4 font-bold">JOURNAL</div>
            <button className="w-40 h-12 m-4 border-bluemed border-4 rounded-full bg-white text-bluemed font-bold">UPDATE <img className='mx-2 h-3 inline' src={plus} alt=''/></button>
          </div>
        </div>
      </div>
    </div>
  )
}
