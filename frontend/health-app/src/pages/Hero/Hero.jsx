import React from 'react'
import logo from "../../assets/logo.png";
import backgroundLogo from "../../assets/logo-lg.png"

export default function Hero() {
  return (
    <div className='bg-gradient-to-b from-customblue h-2screen'>
        <div className='fixed z-10 w-full flex justify-between items-center px-20 h-24' >
            <img src={logo} alt="" className=''/>
            <button className="w-40 h-12 ml-auto mr-3 rounded-full bg-white font-bold">LOG IN</button>
            <button className="w-40 h-12 rounded-full bg-black text-white font-bold">SIGN UP</button>
        </div>
        <div className='relative'>
            <div className='bg-contain bg-no-repeat bg-center h-screen -z-10' style={{backgroundImage:`url(${backgroundLogo})`}}></div>
            <div className="absolute inset-0 flex flex-col min-h-screen justify-center items-center bg-transparent">
                <h1 className='lg:text-9xl md:text-7xl sm:text-5xl text-3xl font-black mb-14'>
                    Reset your mind
                </h1>
                <div className='text-lg mb-14 w-1/4 text-center'>
                    Tracking mental health doesn't have to be tough. Find ways to track your progress and better yourself through Reset.
                </div>
                <button className="w-48 h-14 rounded-full bg-white text-black font-bold">GET STARTED</button>
            </div>
        </div>
        <div className="flex flex-col min-h-screen justify-center items-center">
            <h1 className='lg:text-5xl md:text-5xl sm:text-5xl text-3xl font-black mb-14'>
                ABOUT
            </h1>
            <div className='text-lg mb-20 w-2/4 text-center'>
                Reset is a web application used to help assist individuals needing extra support for their mental health. The application provides ways to track your sleep habits, diet, daily mood, and includes other features to ensure that you are prioritizing and continuously improve your mental well-being.
            </div>
            <div className='text-lg mb-20 w-2/4 text-center'>
                According to the Canadian Centre for Addiction and Mental Health, in any given year, 1 in 5 Canadians experiences a mental illness or addiction problem. Thus, Reset attempts to provide resources and incentivizes citizens to prioritize and track their mental health and well-being.
            </div>
            <div className='text-lg mb-20 w-2/4 text-center'>
                To get started on your improvement journey click the button below to sign up.
            </div>
            <button className="w-48 h-14 rounded-full bg-customblue text-white font-bold">CONTINUE</button>
        </div>
    </div>
  )
}
