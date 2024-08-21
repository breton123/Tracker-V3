import React from "react";

interface WelcomeHeaderProps {
	userName: string;
}

const SetHeader: React.FC<WelcomeHeaderProps> = ({ userName }) => {
	return (
		<div className="w-full h-[50px] relative flex justify-between items-center">
			<div>
				<div className=" text-white text-2xl font-semibold leading-loose ">
					{userName} Trades
				</div>
				<div className=" text-[#adb9e1] text-xs font-normal leading-[14px] ">
					View Set Trades
				</div>
			</div>
		</div>
	);
};

export default SetHeader;
