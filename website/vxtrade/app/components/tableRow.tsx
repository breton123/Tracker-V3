import { Cog6ToothIcon, EyeIcon } from "@heroicons/react/24/solid";
import React from "react";

interface TableRowProps {
	row: {
		[key: string]: string | number | boolean | React.ReactNode;
	};
	isOdd: boolean; // Add this prop
	viewButton: (account: string) => void;
	settingsButton: (
		name: string,
		login: string,
		password: string,
		server: string,
		deposit: string,
		terminalFilePath: string,
		enabled: boolean
	) => void;
}

const TableRow: React.FC<TableRowProps> = ({
	row,
	isOdd,
	viewButton,
	settingsButton,
}) => {
	const openSettings = () => {
		console.log(row);
		settingsButton(
			row.name,
			row.login,
			row.password,
			row.server,
			row.deposit,
			row.terminalFilePath,
			row.enabled
		);
	};

	const viewSets = () => {
		viewButton(row.login.toString());
	};

	return (
		<tr
			className={`h-[61px] text-white text-center ${
				isOdd ? "bg-[#0A1330]" : ""
			}`}>
			{Object.values(row).map((value, idx) => (
				<td key={idx} className="px-2 text-[#AEB9E1]">
					{typeof value === "boolean"
						? value
							? "Yes"
							: "No"
						: value}
				</td>
			))}
			<td>
				<div className="flex justify-center gap-2">
					<EyeIcon
						onClick={viewSets}
						className="text-gray-600 h-5 cursor-pointer hover:scale-125 hover:text-gray-400 transition ease-in-out"
					/>
					<Cog6ToothIcon
						onClick={openSettings}
						className="text-gray-600 h-5 cursor-pointer hover:scale-125 hover:text-gray-400 transition ease-in-out"
					/>
				</div>
			</td>
		</tr>
	);
};

export default TableRow;
