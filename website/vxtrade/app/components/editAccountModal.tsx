import { XCircleIcon } from "@heroicons/react/24/solid";
import React, { useState } from "react";
import addAccount from "../api/methods/addAccount";
import updateAccount from "../api/methods/editAccount";
import ToggleSwitch from "./toggleSwitch";

interface EditAccountModalProps {
	toggleModal: () => void;
	setName: (name: string) => void;
	setLogin: (login: string) => void;
	setPassword: (password: string) => void;
	setServer: (server: string) => void;
	setDeposit: (deposit: string) => void;
	setTerminalFilePath: (terminalFilePath: string) => void;
	setToggleChecked: (checked: boolean) => void;
	username: string;
	defaultName: string;
	defaultLogin: string;
	defaultPassword: string;
	defaultServer: string;
	defaultDeposit: string;
	defaultTerminalFilePath: string;
	defaultToggleChecked: boolean;
}

const EditAccountModal: React.FC<EditAccountModalProps> = ({
	toggleModal,
	username,
	setName,
	defaultName,
	setLogin,
	defaultLogin,
	setPassword,
	defaultPassword,
	setServer,
	defaultServer,
	setDeposit,
	defaultDeposit,
	setTerminalFilePath,
	defaultTerminalFilePath,
	setToggleChecked,
	defaultToggleChecked,
}) => {
	const editAccount = async () => {
		try {
			console.log(defaultToggleChecked);
			const response = await updateAccount(
				defaultName,
				defaultLogin,
				defaultPassword,
				defaultServer,
				defaultDeposit,
				defaultTerminalFilePath,
				defaultToggleChecked,
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
						Edit Account
					</h1>
					<h2 className="text-gray-500 mb-6">
						Edit your account details
					</h2>
					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Name
						</div>
						<input
							type="text"
							value={defaultName}
							className="w-[350px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-gray-500 font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setName(e.target.value)}
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
							disabled={true}
							value={defaultLogin}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setLogin(e.target.value)}
							placeholder="7451935"
							required
						/>
					</div>

					<div className="flex flex-col gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Server
						</div>
						<input
							type="text"
							disabled={true}
							value={defaultServer}
							className="w-[350px] text-gray-500 h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
							onChange={(e) => setServer(e.target.value)}
							placeholder="VantageInternational-Demo"
							required
						/>
					</div>

					<div className="flex gap-2">
						<div className="text-gray-600 text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
							Enabled
						</div>
						<ToggleSwitch
							setIsChecked={setToggleChecked}
							isChecked={defaultToggleChecked}
						/>
					</div>

					<button
						onClick={editAccount}
						className="w-[350px] h-[44.96px] px-2 bg-[#0075ff] rounded-xl backdrop-blur-[120px] flex justify-center items-center">
						<div className="flex-col justify-center items-center inline-flex">
							<div className="h-6 flex justify-center items-center">
								<span className="text-center text-white text-[10px] font-bold font-['Plus Jakarta Display'] leading-[15px]">
									SAVE
								</span>
							</div>
						</div>
					</button>
				</div>
			</div>
		</div>
	);
};

export default EditAccountModal;
