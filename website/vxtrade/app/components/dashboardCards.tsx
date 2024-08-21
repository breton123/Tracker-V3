import {
	ArrowTrendingUpIcon,
	EllipsisHorizontalIcon,
	EyeIcon,
} from "@heroicons/react/24/solid";
import { jwtDecode, JwtPayload } from "jwt-decode";
import React, { useEffect, useState } from "react";
import { useAuth } from "../../context/AuthContext";
import { getCardData } from "../api/methods/getCardData";

interface jwtType extends JwtPayload {
	userId: string;
	email: string;
}

const DashboardCards: React.FC = () => {
	const { user, signOut } = useAuth();
	const [username, setUsername] = useState("");
	const [avgProfit, setAvgProfit] = useState(0);
	const [avgMaxDrawdown, setAvgMaxDrawdown] = useState(0);
	const [avgReturnOnDrawdown, setAvgReturnOnDrawdown] = useState(0);
	const [avgWinRate, setAvgWinRate] = useState(0);
	const [sets, setSets] = useState(0);

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
		const fetchData = async () => {
			try {
				const response = await getCardData(username, 7451935);
				console.log(response);
				setAvgProfit(response["data"]["avgProfit"]);
				setAvgMaxDrawdown(response["data"]["avgMaxDrawdown"]);
				setAvgReturnOnDrawdown(response["data"]["avgReturnOnDrawdown"]);
				setAvgWinRate(response["data"]["avgWinRate"]);
				setSets(response["data"]["sets"]);
			} catch (error) {
				fetchData();
				console.error("Error fetching data:", error);
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
	}, [username]);

	return (
		<div className="flex justify-between gap-4 w-full h-[90px] font-mona px-0 lg:px-10 mt-5">
			<DashboardCard
				title="Avg Profit"
				value={avgProfit.toString()}
				percentage="12.5"
			/>
			<DashboardCard
				title="Avg Max Drawdown"
				value={avgMaxDrawdown.toString()}
				percentage="12.5"
			/>
			<DashboardCard
				title="Avg Return on DD"
				value={avgReturnOnDrawdown.toString()}
				percentage="12.5"
			/>
			<DashboardCard
				title="Avg Win Rate"
				value={avgWinRate.toString()}
				percentage="12.5"
			/>
			<DashboardCard
				title="Sets"
				value={sets.toString()}
				percentage="12.5"
			/>
		</div>
	);
};

type DashboardCardProps = {
	title: string;
	value: string;
	percentage: string;
};

const DashboardCard: React.FC<DashboardCardProps> = ({
	title,
	value,
	percentage,
}) => {
	return (
		<div className="w-[249.46px] h-[100px] relative bg-[#0b1739] rounded-lg border border-[#343a4e] flex flex-col gap-4 items-center justify-center drop-shadow-xl">
			<div className="flex w-full items-center justify-between">
				<div className="px-5 justify-start items-center gap-2 inline-flex">
					<EyeIcon className="h-5 text-[#adb9e1]" />
					<div className="text-[#adb9e1] text-xs font-medium  leading-[14px]">
						{title}
					</div>
				</div>
				<EllipsisHorizontalIcon className="h-6 text-[#adb9e1] pr-3" />
			</div>
			<div className="h-8 w-full px-5 justify-start items-center gap-3 inline-flex">
				<div className="text-white text-2xl font-semibold  leading-loose">
					{value}
				</div>
				<div className="px-1 py-0.5 bg-[#05c168]/20 rounded-sm  h-3/4 items-center border border-[#05c168]/20 flex justify-start gap-1.5 ">
					<div className="text-[#14c973] text-[10px] font-bold  leading-[14px]">
						{percentage}%
					</div>
					<ArrowTrendingUpIcon className="h-4 text-[#14c973]" />
				</div>
			</div>
			<div className="w-4 h-4 left-[193.74px] top-0 absolute">
				<div className="w-3.5 h-[2.44px] left-[1.01px] top-[6.78px] absolute"></div>
			</div>
		</div>
	);
};

export default DashboardCards;
