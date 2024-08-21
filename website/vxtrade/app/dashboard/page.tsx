"use client";

import { jwtDecode, JwtPayload } from "jwt-decode";
import { useEffect, useState } from "react";
import { CircleSpinner } from "react-spinners-kit";
import { useAuth } from "../../context/AuthContext";
import { getSets } from "../api/methods/getSets";
import { getSnapshotsGraph } from "../api/methods/getSnapshotsGraph";
import ChartComponent from "../components/chart";
import DashboardCards from "../components/dashboardCards";
import SideBar from "../components/sideBar";
import Table from "../components/table";
import TotalProfit from "../components/totalProfit";
import WelcomeHeader from "../components/welcomeHeader";

interface jwtType extends JwtPayload {
	userId: string;
	email: string;
}

const Dashboard = () => {
	const { user, signOut } = useAuth();
	const [username, setUsername] = useState("");
	const [data, setData] = useState<string[]>([]);
	const [magics, setMagics] = useState<string[]>([]);
	const [drawdownGraphData, setDrawdownGraphData] = useState<[]>([]);
	const [equityGraphData, setEquityGraphData] = useState<[]>([]);
	const [loading, setLoading] = useState(true);

	const getUser = (user: string) => {
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
		if (username) {
			const fetchData = async () => {
				try {
					const setsResponse = await getSets(username, 7451935);
					const snapshotsResponse = await getSnapshotsGraph(
						username,
						7451935
					);
					const setsResult = setsResponse["data"]["sets"];
					const drawdownGraphData =
						snapshotsResponse["data"]["drawdownData"];
					const equtiyGraphData =
						snapshotsResponse["data"]["equityData"];
					const magicsResponse = snapshotsResponse["data"]["magics"];
					//const snapshotResult = snapshotsResponse["data"]["sets"];
					setDrawdownGraphData(drawdownGraphData);
					setEquityGraphData(equtiyGraphData);
					setMagics(magicsResponse);
					if (setsResult.length > 0) {
						setData(setsResult);
					}
				} catch (error) {
					console.error("Error fetching data:", error);
				} finally {
					setLoading(false);
				}
			};
			fetchData();
		}
	}, [username]);

	return (
		<div className="w-full h-full min-h-screen relative font-mona ">
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			<div className="w-full h-full absolute bg-gradient-to-b from-[#0f123b] via-[#080c2d] to-[#020515]" />
			<div className="flex">
				<SideBar />
				{loading ? (
					<div className="flex flex-col items-center opacity-60 h-screen justify-center w-full px-10 py-16 gap-5 fill-white">
						<CircleSpinner color="#cb3cff" loading={loading} />
					</div>
				) : (
					<div className="flex flex-col w-full px-10 py-16 gap-5">
						<WelcomeHeader userName={username} />
						<DashboardCards />
						<div className="flex justify-center mt-5 px-0 lg:px-10 ">
							<ChartComponent
								magics={magics}
								data={equityGraphData}
								title="Equity"
							/>
							<div className="flex flex-col w-1/3">
								<TotalProfit />
								<TotalProfit />
							</div>
						</div>
						<div className="px-10">
							<Table data={data} title="Open Sets" />
						</div>
					</div>
				)}
				;
			</div>
		</div>
	);
};

export default Dashboard;
