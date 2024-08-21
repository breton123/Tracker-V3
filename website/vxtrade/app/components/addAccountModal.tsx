import { XCircleIcon } from "@heroicons/react/24/solid";
import React, { useState } from "react";
import addAccount from "../api/methods/addAccount";
import ToggleSwitch from "./toggleSwitch";

interface AddAccountModalProps {
	toggleModal: () => void;
	username: string;
}

const AddAccountModal: React.FC<AddAccountModalProps> = ({
	toggleModal,
	username,
}) => {
	const [accountName, setAccountName] = useState<string>("");
	const [accountLogin, setAccountLogin] = useState<string>("");
	const [accountPassword, setAccountPassword] = useState<string>("");
	const [accountServer, setAccountServer] = useState<string>("");
	const [accountDeposit, setAccountDeposit] = useState<string>("");
	const [accountTerminalFilePath, setAccountTerminalFilePath] =
		useState<string>("");

	const createAccount = async () => {
		try {
			const response = await addAccount(
				accountName,
				accountLogin,
				accountPassword,
				accountServer,
				accountDeposit,
				accountTerminalFilePath,
				username
			);
			console.log(response);
			toggleModal();
		} catch (error) {
			console.error("Error fetching data:", error);
		}
	};

	return (
		<div className="flex items-center w-full justify-center h-full absolute z-0 bg-gray-50 bg-opacity-20 backdrop-blur-sm">
			<div className="w-1/2 h-3/4 bg-white rounded-2xl shadow-xl flex p-10 flex-col">
				<div className="flex">
					<XCircleIcon
						onClick={toggleModal}
						className="h-10 fill-gray-400 hover:fill-red-600 transition ease-in-out cursor-pointer"
					/>
				</div>
				<div className="flex flex-col gap-3 w-full items-center h-full justify-center">
					<h1 className="text-gray-600 font-semibold text-3xl">
						Add an account
					</h1>
					<h2 className="text-gray-500 mb-6">
						Enter your account details to start tracking
					</h2>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Name
						</div>
						<input
							type="text"
							value={accountName}
							className="w-[350px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-gray-500 font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setAccountName(e.target.value)}
							placeholder="Account Name"
							required
						/>
					</div>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Login
						</div>
						<input
							type="text"
							value={accountLogin}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setAccountLogin(e.target.value)}
							placeholder="7451935"
							required
						/>
					</div>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Password
						</div>
						<input
							type="password"
							value={accountPassword}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setAccountPassword(e.target.value)}
							placeholder="Your password"
							required
						/>
					</div>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Server
						</div>
						<input
							type="text"
							value={accountServer}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setAccountServer(e.target.value)}
							placeholder="VantageInternational-Demo"
							required
						/>
					</div>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Deposit
						</div>
						<input
							type="number"
							value={accountDeposit}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setAccountDeposit(e.target.value)}
							placeholder="100000"
							required
						/>
					</div>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Terminal File Path (path to terminal64.exe)
						</div>
						<input
							type="text"
							value={accountTerminalFilePath}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) =>
								setAccountTerminalFilePath(e.target.value)
							}
							placeholder="C:\Program Files\MetaTrader 5\terminal64.exe"
							required
						/>
					</div>
					<div className="flex gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Enabled
						</div>
						<ToggleSwitch />
					</div>

					<button
						onClick={createAccount}
						className="w-[350px] h-[44.96px] px-2 bg-[#0075ff] rounded-xl backdrop-blur-[120px] flex justify-center items-center">
						<div className="flex-col justify-center items-center inline-flex">
							<div className="h-6 flex justify-center items-center">
								<span className="text-center text-white text-[10px] font-bold font-['Plus Jakarta Display'] leading-[15px]">
									ADD ACCOUNT
								</span>
							</div>
						</div>
					</button>
				</div>
			</div>
		</div>
	);
};

export default AddAccountModal;
