"use client";

import React, { createContext, useContext, useEffect, useState } from "react";

interface AuthContextType {
	user: any;
	signIn: (email: string, password: string) => void;
	signOut: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
	children,
}) => {
	const [user, setUser] = useState<any>(null);

	useEffect(() => {
		const token = localStorage.getItem("authToken");
		if (token) {
			// Optionally fetch user data with token
			setUser({ token }); // Set user data here
		}
	}, []);

	const signIn = async (email: string, password: string) => {
		const response = await fetch("/api/auth/signin", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ email, password }),
		});

		const data = await response.json();
		if (response.ok) {
			localStorage.setItem("authToken", data.token);
			setUser({ token: data.token });
		}
	};

	const signOut = () => {
		localStorage.removeItem("authToken");
		setUser(null);
	};

	return (
		<AuthContext.Provider value={{ user, signIn, signOut }}>
			{children}
		</AuthContext.Provider>
	);
};

export const useAuth = () => {
	const context = useContext(AuthContext);
	if (context === undefined) {
		throw new Error("useAuth must be used within an AuthProvider");
	}
	return context;
};
