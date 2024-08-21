import React from "react";

interface WelcomeHeaderProps {
	userName: string;
}

const AccountsHeader: React.FC<WelcomeHeaderProps> = ({ userName }) => {
	return (
		<div className="w-full h-[50px] relative flex justify-between items-center">
			<div>
				<div className=" text-white text-2xl font-semibold leading-loose ">
					{userName} Accounts
				</div>
				<div className=" text-[#adb9e1] text-xs font-normal leading-[14px] ">
					View, Edit or Create an Account
				</div>
			</div>
			<div className="h-[30px] flex items-start gap-3">
				<div className="p-2 bg-[#cb3cff] rounded flex justify-center items-center gap-1.5 cursor-pointer">
					<div className="text-center text-white text-xs font-medium leading-[14px] ">
						Add Account
					</div>
				</div>
			</div>
		</div>
	);
};

export default AccountsHeader;
