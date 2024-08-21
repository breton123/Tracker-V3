"use client";

import { ChevronDownIcon } from "@heroicons/react/24/solid";
import { jwtDecode, JwtPayload } from "jwt-decode";
import { useEffect, useState } from "react";
import { CircleSpinner } from "react-spinners-kit";
import { useAuth } from "../../context/AuthContext";
import { getAccounts } from "../api/methods/getAccounts";
import { getSets } from "../api/methods/getSets";
import { getSnapshots } from "../api/methods/getSnapshots";
import { getSnapshotsGraph } from "../api/methods/getSnapshotsGraph";
import Chart from "../components/chart";
import SetsTable from "../components/profileSetsTable";
import SetLoader from "../components/setLoader";
import SetLoaderHeader from "../components/setLoaderHeader";
import SetsHeader from "../components/setsHeader";
import SideBar from "../components/sideBar";
import Table from "../components/table";

type DataRow = {
	[key: string]: string | number | boolean | React.ReactNode;
};

interface jwtType extends JwtPayload {
	userId: string;
	email: string;
}

const Sets = () => {
	const { user } = useAuth();
	const [loading, setLoading] = useState<boolean>(true);
	const [username, setUsername] = useState<string | null>(null);
	const [messages, setMessages] = useState([]);
	const [account, setAccount] = useState<number>(7451935);
	const [selectedProfile, setSelectedProfile] = useState<string | boolean>(
		false
	);
	const [files, setFiles] = useState<File[]>([]);
	const [profileDropdown, setProfileDropdown] = useState<boolean>(false);
	const [controllerConnected, setControllerConnected] =
		useState<boolean>(true);
	const [profile, setProfile] = useState<string | null>(null);
	const [profiles, setProfiles] = useState<string[]>([]);
	const [ws, setWs] = useState<WebSocket | null>(null); // WebSocket state
	const [apiKey, setAPIKey] = useState<string>("");
	const [expertName, setExpertName] = useState<string>("");
	const [symbolSuffix, setSymbolSuffix] = useState<string>("");
	const [data, setData] = useState<DataRow[]>([]);

	useEffect(() => {
		// Get the hash from the URL
		const hash = window.location.hash;

		// Check if the hash contains an id
		if (hash.includes("id=")) {
			// Extract the id value from the hash
			const idValue = new URLSearchParams(hash.substring(1)).get("id");
			setAccount(Number(idValue));
		}
	}, []); // Empty dependency array ensures this runs once on component mount

	useEffect(() => {
		setLoading(true);
		// Create a new WebSocket connection
		const websocket = new WebSocket(
			`ws://localhost:8000/ws?username=${username}`
		);
		setWs(websocket);
		// Handle the WebSocket connection open event
		websocket.onopen = () => {
			console.log("WebSocket connection opened");
			// Optionally send a message after the connection is established
			websocket.send(
				JSON.stringify({
					type: "connect",
					username,
					source: "app",
					account: account,
				})
			);

			setLoading(false);
		};

		// Handle incoming messages
		websocket.onmessage = (event) => {
			const message = JSON.parse(event.data);
			if (message.message == "Set Data") {
				setProfile(message.previousProfile);
				setSelectedProfile(message.previousProfile);
				setProfiles(message.profiles);
				setData(message.profileSets);
			}
			// Update the state with the new message
			console.log(message);
			setControllerConnected(message.controller);
		};

		// Handle WebSocket errors
		websocket.onerror = (error) => {
			console.error("WebSocket error:", error);
		};

		// Handle the WebSocket connection close event
		websocket.onclose = () => {
			console.log("WebSocket connection closed");
		};

		// Cleanup the WebSocket connection when the component unmounts
		return () => {
			websocket.close();
		};
	}, [username, account]); // Only re-run this effect if the username changes

	const getUser = (user: string) => {
		setLoading(true);
		const userData: jwtType = jwtDecode(user);
		if (userData.userId) {
			setUsername(userData.userId);
		}
	};

	useEffect(() => {
		if (user) {
			getUser(user.token);
		}
	}, [user]);

	// Button click handler to send a message
	const sendMessage = () => {
		if (ws && ws.readyState === WebSocket.OPEN) {
			ws.send(
				JSON.stringify({
					newData: false,
					profile: profile,
					account: account,
				})
			);
		}
	};

	const toggleDropdown = () => {
		if (profileDropdown) {
			setProfileDropdown(false);
		} else {
			setProfileDropdown(true);
		}
	};

	const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		if (event.target.files) {
			setFiles(Array.from(event.target.files));
		}
	};

	const handleUpload = async () => {
		if (ws && ws.readyState === WebSocket.OPEN) {
			const fileDataPromises = files.map((file) => {
				return new Promise<{ name: string; data: string }>(
					(resolve) => {
						const reader = new FileReader();
						reader.onload = () => {
							resolve({
								name: file.name,
								data: reader.result as string, // file content as text
							});
						};
						reader.readAsText(file); // Read file as text
					}
				);
			});

			const fileData = await Promise.all(fileDataPromises);

			// Create a structured message
			const message = JSON.stringify({
				type: "upload",
				files: fileData,
				account: account,
				profile: selectedProfile,
				apiKey: apiKey,
				expertName: expertName,
				symbolSuffix: symbolSuffix,
			});

			ws.send(message);
			console.log("Files sent:", fileData);
		} else {
			console.warn("WebSocket is not open. Message not sent.");
		}
	};
	return (
		<div className="w-full h-full min-h-screen relative">
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			<div className="flex">
				<SideBar />

				<div className="flex flex-col w-screen px-10 py-16 gap-5">
					{loading ? (
						<div className="flex flex-col items-center opacity-60 h-screen justify-center w-full px-10 py-16 gap-5 fill-white">
							<CircleSpinner color="#cb3cff" loading={loading} />
						</div>
					) : (
						<div className="flex flex-col w-full gap-5 overflow-x-clip">
							<SetLoaderHeader
								userName={account.toString() || ""}
							/>
							{!controllerConnected ? (
								<div className="flex flex-col items-center opacity-60 justify-center w-full px-10 py-16 gap-5 fill-white">
									<h1 className="text-white">
										Trying to connect to controller
									</h1>
									<CircleSpinner
										color="#cb3cff"
										loading={!controllerConnected}
									/>
								</div>
							) : (
								<div className="flex justify-start items-start opacity-90 w-full gap-5 fill-white bg-[#0b1739] rounded-xl shadow border border-[#343a4e]">
									<div className="w-1/4 border-r py-16 border-[#343a4e] flex flex-col items-center gap-5">
										<h1 className="text-white">
											Set Loader
										</h1>
										<div className="flex flex-col items-center justify-center">
											<div
												tabIndex={0}
												role="button"
												onClick={toggleDropdown}
												className="btn m-1 text-white bg-gray-400 bg-opacity-40 px-2 py-1 rounded-md flex items-center gap-1">
												<h1>{selectedProfile}</h1>
												<ChevronDownIcon className="h-5" />
											</div>

											{profileDropdown ? (
												<ul
													tabIndex={0}
													className="dropdown-content text-white menu bg-base-100 rounded-box z-[1] w-52 p-2 shadow items-center">
													{profiles.map(
														(profile, index) => (
															<li
																key={index}
																className="flex w-full justify-center cursor-pointer"
																onClick={() => {
																	setSelectedProfile(
																		profile
																	);
																	setProfileDropdown(
																		false
																	);
																}} // Pass function reference
															>
																<a>{profile}</a>
															</li>
														)
													)}
												</ul>
											) : (
												<span></span>
											)}
											<input
												type="file"
												multiple
												onChange={handleFileChange}
												className="text-white mt-5"
											/>
											<input
												type="text"
												value={apiKey}
												className="w-[200px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-white font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input mt-5"
												onChange={(e) =>
													setAPIKey(e.target.value)
												}
												placeholder="Your POW API Key"
												required
											/>
											<input
												type="text"
												value={expertName}
												className="w-[200px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-white font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input mt-5"
												onChange={(e) =>
													setExpertName(
														e.target.value
													)
												}
												placeholder="Expert name (.ex5)"
												required
											/>
											<input
												type="text"
												value={symbolSuffix}
												className="w-[200px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-white font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input mt-5"
												onChange={(e) =>
													setSymbolSuffix(
														e.target.value
													)
												}
												placeholder="Symbol Suffix)"
												required
											/>
											<button
												onClick={handleUpload}
												className="text-white mt-5 p-2 bg-[#cb3cff] rounded text-xs font-medium leading-[14px]">
												Upload Files
											</button>
										</div>
									</div>
									<SetsTable data={data} />
								</div>
							)}
						</div>
					)}
				</div>
			</div>
		</div>
	);
};

export default Sets;
