"use client";

import { jwtDecode, JwtPayload } from "jwt-decode";
import { useEffect, useState } from "react";
import { CircleSpinner } from "react-spinners-kit";
import { useAuth } from "../../context/AuthContext";
import { getAccounts } from "../api/methods/getAccounts";
import { getSets } from "../api/methods/getSets";
import { getSnapshots } from "../api/methods/getSnapshots";
import { getSnapshotsGraph } from "../api/methods/getSnapshotsGraph";
import { getTrades } from "../api/methods/getTrades";
import Chart from "../components/chart";
import SetHeader from "../components/setHeader";
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
	const [data, setData] = useState<DataRow[]>([]);
	const [account, setAccount] = useState<number>(7451935);
	const [magic, setMagic] = useState<number>(2516);
	const [magics, setMagics] = useState<string[]>([]);
	const [drawdownGraphData, setDrawdownGraphData] = useState([]);
	const [equityGraphData, setEquityGraphData] = useState([]);
	const [loading, setLoading] = useState<boolean>(true);
	const [username, setUsername] = useState<string | null>(null);

	const getUser = (user: string) => {
		setLoading(true);
		const userData: jwtType = jwtDecode(user);
		if (userData.userId) {
			setUsername(userData.userId);
		}
	};

	useEffect(() => {
		// Get the hash from the URL
		const hash = window.location.hash;

		// Check if the hash contains an id
		if (hash.includes("id=") && hash.includes("magic=")) {
			// Extract the id value from the hash
			const idValue = new URLSearchParams(hash.substring(1)).get("id");
			setAccount(Number(idValue));
			const magicValue = new URLSearchParams(hash.substring(1)).get(
				"magic"
			);
			setMagic(Number(magicValue));
		}
	}, []); // Empty dependency array ensures this runs once on component mount

	useEffect(() => {
		if (user) {
			getUser(user.token);
		}
	}, [user]);

	useEffect(() => {
		if (username) {
			const fetchData = async () => {
				try {
					const tradesResponse = await getTrades(
						username,
						account,
						magic
					);
					if (tradesResponse["data"]["trades"].length > 0) {
						setData(tradesResponse["data"]["trades"]);
					}
				} catch (error) {
					console.error("Error fetching data:", error);
				} finally {
					setLoading(false);
				}
			};
			fetchData();
		}
	}, [username, account]);

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
							<SetHeader userName={magic.toString() || ""} />
							<div className="bg-[#0b1739] rounded-xl shadow border border-[#343a4e] overflow-x-auto">
								{/* The overflow-x-auto ensures horizontal scrolling */}
								<Table data={data} title="Trades" />
							</div>
							<Chart
								data={drawdownGraphData}
								magics={magics}
								title="Drawdown"
							/>
							<Chart
								data={equityGraphData}
								magics={magics}
								title="Equity"
							/>
						</div>
					)}
				</div>
			</div>
		</div>
	);
};

export default Sets;
