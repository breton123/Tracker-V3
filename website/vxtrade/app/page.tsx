import React from "react";
import "./globals.css"; // Ensure the path is correct
import SignInForm from "./signin/page"; // Adjust import based on your directory

export default function Home() {
	return (
		<div className="h-screen font-dm">
			<SignInForm />
		</div>
	);
}
