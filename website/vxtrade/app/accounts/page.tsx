"use client";

import { XCircleIcon } from "@heroicons/react/24/solid";
import { jwtDecode, JwtPayload } from "jwt-decode";
import { CSSProperties, useEffect, useState } from "react";
import { CircleSpinner, FlagSpinner } from "react-spinners-kit";
import { useAuth } from "../../context/AuthContext";
import addAccount from "../api/methods/addAccount";
import { getAccounts } from "../api/methods/getAccounts";
import AccountsHeader from "../components/accountsHeader";
import AddAccountModal from "../components/addAccountModal";
import EditAccountModal from "../components/editAccountModal";
import SideBar from "../components/sideBar";
import Table from "../components/table";
import ToggleSwitch from "../components/toggleSwitch";

type DataRow = {
	[key: string]: string | number | boolean | React.ReactNode;
};

interface jwtType extends JwtPayload {
	userId: string;
	email: string;
}

const Accounts = () => {
	const { user, signOut } = useAuth();
	const [data, setData] = useState<DataRow[]>([]);
	const [loading, setLoading] = useState<boolean>(true);
	const [username, setUsername] = useState("");
	const [accountModal, setAccountModal] = useState(false);
	const [editModal, setEditModal] = useState(false);

	const [editName, setEditName] = useState<string>("");
	const [editLogin, setEditLogin] = useState<string>("");
	const [editPassword, setEditPassword] = useState<string>("");
	const [editServer, setEditServer] = useState<string>("");
	const [editDeposit, setEditDeposit] = useState<string>("");
	const [editToggleChecked, setEditToggleChecked] = useState<boolean>(false);
	const [editTerminalFilePath, setEditTerminalFilePath] =
		useState<string>("");

	const getUser = (user: string) => {
		setLoading(true);
		const userData: jwtType = jwtDecode(user);
		console.log(userData);
		if (userData.userId) {
			setUsername(userData.userId);
		}
	};

	useEffect(() => {
		if (user) {
			getUser(user.token);
		}
	}, [user]);

	useEffect(() => {
		setLoading(true);
		const fetchData = async () => {
			try {
				const response = await getAccounts(username);
				const result = response["data"]["accounts"];
				console.log(response);
				setData(result);
			} catch (error) {
				fetchData();
				console.error("Error fetching data:", error);
			} finally {
				setLoading(false);
			}
		};
		if (
			username != null &&
			username.length > 0 &&
			username != undefined &&
			username != ""
		) {
			fetchData();
		}
	}, [username, accountModal, editModal]);

	const toggleAccountModal = () => {
		if (accountModal) {
			setAccountModal(false);
		} else {
			setAccountModal(true);
		}
	};

	const toggleEditModal = () => {
		if (editModal) {
			setEditModal(false);
		} else {
			setEditModal(true);
		}
	};

	const openEditModal = (
		name: string,
		login: string,
		password: string,
		server: string,
		deposit: string,
		terminalFilePath: string,
		toggleChecked: boolean
	) => {
		setEditName(name);
		setEditLogin(login);
		setEditPassword(password);
		setEditServer(server);
		setEditDeposit(deposit);
		setEditTerminalFilePath(terminalFilePath);
		setEditToggleChecked(toggleChecked);
		setEditModal(true);
	};

	const viewSets = (account: string) => {
		window.location.href = "/sets#id=" + account;
	};

	return (
		<div className="w-full h-full min-h-screen relative">
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			{accountModal ? (
				<div className="z-10 fixed inset-0">
					<AddAccountModal
						toggleModal={toggleAccountModal}
						username={username}
					/>
				</div>
			) : (
				<span></span>
			)}
			{editModal ? (
				<div className="z-10 fixed inset-0">
					<EditAccountModal
						toggleModal={toggleEditModal}
						username={username}
						setName={setEditName}
						defaultName={editName}
						setLogin={setEditLogin}
						defaultLogin={editLogin}
						setPassword={setEditPassword}
						defaultPassword={editPassword}
						setServer={setEditServer}
						defaultServer={editServer}
						setDeposit={setEditDeposit}
						defaultDeposit={editDeposit}
						setTerminalFilePath={setEditTerminalFilePath}
						defaultTerminalFilePath={editTerminalFilePath}
						setToggleChecked={setEditToggleChecked}
						defaultToggleChecked={editToggleChecked}
					/>
				</div>
			) : (
				<span></span>
			)}

			<div className="flex ">
				<SideBar />

				{loading ? (
					<div className="flex flex-col items-center opacity-60 h-screen justify-center w-full px-10 py-16 gap-5 fill-white">
						<CircleSpinner color="#cb3cff" loading={loading} />
					</div>
				) : (
					<div className="flex flex-col w-full px-10 py-16 gap-5">
						<div className="w-full h-[50px] relative flex justify-between items-center">
							<div>
								<div className=" text-white text-2xl font-semibold leading-loose ">
									{username} Accounts
								</div>
								<div className=" text-[#adb9e1] text-xs font-normal leading-[14px] ">
									View, Edit or Create an Account
								</div>
							</div>
							<div className="h-[30px] flex items-start gap-3">
								<div
									onClick={toggleAccountModal}
									className="p-2 bg-[#cb3cff] rounded flex justify-center items-center gap-1.5 cursor-pointer">
									<div className="text-center text-white text-xs font-medium leading-[14px] ">
										Add Account
									</div>
								</div>
							</div>
						</div>
						<Table
							data={data}
							title="Accounts"
							viewButton={viewSets}
							settingsButton={openEditModal}
						/>
					</div>
				)}
			</div>
		</div>
	);
};

export default Accounts;
