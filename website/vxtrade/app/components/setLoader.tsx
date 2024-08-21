import React from "react";

interface WelcomeHeaderProps {
	userName: string;
}

const SetLoader: React.FC<WelcomeHeaderProps> = ({ userName }) => {
	return (
		<div className="w-full h-[200px] bg-[#0b1739] rounded-tl-xl rounded-bl-xl border border-[#343a4e]">
			<h1 className="text-white">Hello</h1>
		</div>
	);
};

export default SetLoader;
