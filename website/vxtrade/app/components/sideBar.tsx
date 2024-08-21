"use client";

import {
	ArrowLeftStartOnRectangleIcon,
	ArrowsRightLeftIcon,
	ArrowUpTrayIcon,
	CodeBracketIcon,
	Cog6ToothIcon,
	Cog8ToothIcon,
	ComputerDesktopIcon,
	CurrencyDollarIcon,
	HomeIcon,
	NewspaperIcon,
	UserIcon,
} from "@heroicons/react/24/outline";
import Image from "next/image";
import { useRouter } from "next/router";
import React from "react";

interface NavItemProps {
	title: string;
	active?: boolean;
	highlighted?: boolean;
	Icon: React.ElementType;
	href: string; // Add href to NavItemProps
}

const SideBar: React.FC = () => {
	const [path, setPath] = React.useState<string>("");

	React.useEffect(() => {
		// Update path on mount
		setPath(window.location.pathname);

		// Optionally, listen to URL changes (e.g., for Single Page Application)
		const handleLocationChange = () => setPath(window.location.pathname);

		window.addEventListener("popstate", handleLocationChange);

		return () => {
			window.removeEventListener("popstate", handleLocationChange);
		};
	}, []);

	const navItems = [
		{ title: "Dashboard", icon: HomeIcon, href: "/dashboard" },
		{ title: "Accounts", icon: ComputerDesktopIcon, href: "/accounts" },
		{ title: "Sets", icon: NewspaperIcon, href: "/sets" },
		{ title: "Set Loader", icon: ArrowUpTrayIcon, href: "/" },
		{ title: "Settings", icon: Cog6ToothIcon, href: "/" },
		{ title: "Users", icon: UserIcon, href: "/" },
		{ title: "Pricing", icon: CurrencyDollarIcon, href: "/" },
		{ title: "Integrations", icon: ArrowsRightLeftIcon, href: "/" },
	];

	return (
		<div className="w-[350px] h-screen relative flex flex-col gap-10 bg-[#081028] bg-opacity-30 drop-shadow-xl justify-start pl-5 py-5">
			<div className="flex items-center justify-between px-3">
				<Logo />
				<CodeBracketIcon className="h-5 text-[#AEB9E1] transition ease-in-out opacity-30 hover:text-white cursor-pointer hover:opacity-100" />
			</div>
			<div className="w-full">
				<SearchBar />
			</div>

			<div className="flex flex-col justify-between gap-16 w-full">
				<div className="flex flex-col gap-2 font-semibold">
					{navItems.map(({ title, icon: Icon, href }) => (
						<a key={title} href={href}>
							<NavItem
								title={title}
								Icon={Icon}
								active={path === href} // Set active based on the current path
								href={href}
							/>
						</a>
					))}
				</div>
				<div className="flex flex-col gap-2">
					<NavItem
						title="Account Settings"
						Icon={Cog8ToothIcon}
						href="/"
					/>
					<NavItem
						title="Sign Out"
						Icon={ArrowLeftStartOnRectangleIcon}
						href="/"
					/>
				</div>
			</div>
		</div>
	);
};

const NavItem: React.FC<NavItemProps> = ({ title, active, Icon }) => {
	return (
		<div
			className={`relative ${
				active
					? "text-[#cb3cff] bg-[#7e89ac] border-[#0a1330] border-opacity-10 bg-opacity-5"
					: "text-[#adb9e1] hover:bg-[#7e89ac] hover:border-[#0a1330] hover:border-opacity-10 hover:bg-opacity-5"
			} rounded-[7px] flex items-baseline justify-start px-4 py-2 w-[90%] h-10 cursor-pointer
                transition ease-in-out group`}>
			<Icon className="h-5 pr-2 translate-y-[2px] group-hover:text-white transition ease-in-out" />
			<span
				className={`${
					active
						? "text-sm font-medium text-[#cb3cff]"
						: "text-sm font-medium text-[#adb9e1] group-hover:text-white transition ease-in-out"
				}`}>
				{title}
			</span>
			<div
				className={`${
					active
						? "w-[3.19px] h-full bg-[#cb3cff] absolute left-0 top-[-0.95px] rounded-l opacity-100 transition ease-in-out"
						: "w-[3.19px] h-full bg-[#cb3cff] absolute left-0 top-[-0.95px] rounded-l opacity-0 transition ease-in-out group-hover:opacity-100"
				}`}></div>
		</div>
	);
};

const SearchBar: React.FC = () => {
	return (
		<div className="w-[90%] h-[42px] bg-[#0b1739] rounded border border-[#343a4e] flex items-center px-4">
			<div className="flex items-center gap-2">
				<div className="w-4 h-4">{/* Placeholder icon */}</div>
				<span className="text-[#adb9e1] text-xs font-medium">
					Search for...
				</span>
			</div>
		</div>
	);
};

const Logo: React.FC = () => {
	return (
		<div className="flex items-center">
			<Image src="/logo.png" alt="My Image" width={30} height={20} />
			<span className="text-white text-xl font-semibold ml-2">
				VXTrade
			</span>
		</div>
	);
};

export default SideBar;
