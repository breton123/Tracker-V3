"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import ToggleSwitch from "../components/toggleSwitch";

const SignInForm = () => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const router = useRouter();

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();

		const response = await fetch("/api/auth/signin", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ email, password }),
		});

		const data = await response.json();
		if (response.ok) {
			localStorage.setItem("authToken", data.token); // Save token
			router.push("/dashboard"); // Redirect after sign-in
		} else {
			alert(data.message);
		}
	};

	return (
		<div className="flex w-full h-full bg-gradient-to-r from-[#0F123B] via-[#090D2E] to-[#020515]">
			<div className="w-1/2 bg-red-50 m-24"></div>
			<div className="w-1/2 flex h-full justify-center items-center">
				<form
					onSubmit={handleSubmit}
					className="flex flex-col w-1/2 gap-3 items-start justify-start">
					<h1 className="text-white font-semibold text-3xl w-full">
						Nice to see you!
					</h1>
					<h2 className="text-gray-300 mb-6">
						Enter your email and password to sign in
					</h2>
					<div className="text-white text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
						Email
					</div>
					<input
						type="text"
						value={email}
						className="w-[350px] h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal text-white font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
						onChange={(e) => setEmail(e.target.value)}
						placeholder="Your Username or Email"
						required
					/>
					<div className="text-white text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
						Password
					</div>
					<input
						type="password"
						value={password}
						className="w-[350px] text-white h-[49.96px] px-5 rounded-[20px] border-2 border-[#151515] backdrop-blur-[42px] placeholder:text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight flex items-center flex-shrink-0 custom-input"
						onChange={(e) => setPassword(e.target.value)}
						placeholder="Your password"
						required
					/>
					<div className="flex gap-4 my-3">
						<ToggleSwitch />
						<p className="text-white text-sm">Remember me</p>
					</div>

					<button
						type="submit"
						className="w-[350px] h-[44.96px] px-2 bg-[#0075ff] rounded-xl backdrop-blur-[120px] flex justify-center items-center">
						<div className="flex-col justify-center items-center inline-flex">
							<div className="h-6 flex justify-center items-center">
								<span className="text-center text-white text-[10px] font-bold font-['Plus Jakarta Display'] leading-[15px]">
									SIGN IN
								</span>
							</div>
						</div>
					</button>
					<div className="w-3/4 flex justify-center">
						<div className="text-center items-center">
							<span className="text-[#a0aec0] text-sm font-normal font-['Plus Jakarta Display'] leading-tight">
								Don't have an account?{"  "}
							</span>
							<span className="text-white text-sm font-bold font-['Plus Jakarta Display'] leading-tight">
								Sign up
							</span>
						</div>
					</div>
				</form>
			</div>
		</div>
	);
};

export default SignInForm;
