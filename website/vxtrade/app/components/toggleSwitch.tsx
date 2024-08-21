import React, { useState } from "react";
import "../globals.css"; // Ensure this is correctly imported if you have additional styles

interface ToggleProps {
	setIsChecked: (isChecked: boolean) => void;
	isChecked: boolean;
}

const ToggleSwitch: React.FC<ToggleProps> = ({ setIsChecked, isChecked }) => {
	const handleChange = (e: {
		target: { checked: boolean | ((prevState: boolean) => boolean) };
	}) => {
		setIsChecked(e.target.checked);
	};

	return (
		<label className="relative inline-flex items-center cursor-pointer">
			<input
				type="checkbox"
				checked={isChecked}
				onChange={handleChange}
				className="sr-only" // Hide the default checkbox
			/>
			<div
				className={`w-9 h-[18.48px] bg-[#0075ff] rounded-[97.74px] flex items-center p-[1.44px] transition-colors duration-300 ${
					isChecked ? "bg-blue-500" : "bg-gray-300"
				}`}>
				<div
					className={`w-[13.50px] h-[13.50px] bg-white rounded-full transition-transform duration-300 ${
						isChecked ? "translate-x-4" : "translate-x-0"
					}`}
				/>
			</div>
		</label>
	);
};

export default ToggleSwitch;
