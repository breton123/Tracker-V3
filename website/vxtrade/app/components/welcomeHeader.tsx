import React from "react";

interface WelcomeHeaderProps {
	userName: string;
	onExportData?: () => void;
	onCreateReport?: () => void;
}

const WelcomeHeader: React.FC<WelcomeHeaderProps> = ({
	userName,
	onExportData,
	onCreateReport,
}) => {
	return (
		<div className="w-full h-[50px] relative flex justify-between items-center">
			<div>
				<div className=" text-white text-2xl font-semibold leading-loose ">
					Welcome back, {userName}
				</div>
				<div className=" text-[#adb9e1] text-xs font-normal leading-[14px] ">
					Measure your advertising ROI and report website traffic.
				</div>
			</div>
			<div className="h-[30px] flex items-start gap-3">
				<div
					className="p-2 bg-[#0a1330] rounded flex justify-center items-center gap-1.5 cursor-pointer"
					onClick={onExportData}>
					<div className="text-center text-white text-xs font-medium leading-[14px] ">
						Export data
					</div>
					<div className="relative w-2.5 h-2.5">
						{/* Add any icon or SVG inside this div if needed */}
						<div className="absolute top-0 left-[0.91px] w-[8.18px] h-2.5"></div>
					</div>
				</div>
				<div
					className="p-2 bg-[#cb3cff] rounded flex justify-center items-center gap-1.5 cursor-pointer"
					onClick={onCreateReport}>
					<div className="text-center text-white text-xs font-medium leading-[14px] ">
						Create report
					</div>
				</div>
			</div>
		</div>
	);
};

export default WelcomeHeader;
