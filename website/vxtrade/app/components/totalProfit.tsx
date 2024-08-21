import { ArrowTrendingUpIcon } from "@heroicons/react/24/solid";
import React, { useState } from "react";
import "../globals.css"; // Ensure this is correctly imported if you have additional styles
import BarChartComponent from "./barChart";
import ChartBar from "./chartBar";

const TotalProfit = () => {
	const generateRandomNumber = (min: number, max: number): number => {
		return Math.floor(Math.random() * (max - min + 1)) + min;
	};
	const randomNumbersArray = Array(24)
		.fill(0)
		.map(() => generateRandomNumber(50, 50));

	return (
		<div className=" h-1/2 relative font-mona w-full bg-[#0b1739] rounded-tr-xl border border-[#343a4e]">
			<div className="w-full h-full flex flex-col p-3">
				<div className="justify-start items-center gap-1.5 inline-flex mb-1">
					<ArrowTrendingUpIcon className="text-[#adb9e1] h-5" />
					<div className="text-[#adb9e1] text-xs font-medium  leading-[14px]">
						Total profit
					</div>
				</div>
				<div className="h-8 w-full justify-start items-center gap-3 inline-flex">
					<div className="text-white text-2xl font-semibold  leading-loose">
						$1,452
					</div>
					<div className="px-1 py-0.5 bg-[#05c168]/20 rounded-sm  h-3/4 items-center border border-[#05c168]/20 flex justify-start gap-1.5 ">
						<div className="text-[#14c973] text-[10px] font-bold  leading-[14px]">
							28.4%
						</div>
						<ArrowTrendingUpIcon className="h-4 text-[#14c973]" />
					</div>
				</div>
				<div className="w-full h-[171.47px] -translate-y-5">
					<div className="w-full h-[93.36px]">
						<BarChartComponent />
					</div>
				</div>
				<div className="w-full h-[27.71px]">
					<div className="w-full h-3.5 flex justify-between items-center">
						<div className="text-right text-[#cb3cff] text-xs font-normal  leading-[14px]">
							View report
						</div>
						<div className="text-[#adb9e1] text-xs font-normal  leading-[14px]">
							Last 12 months
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default TotalProfit;
