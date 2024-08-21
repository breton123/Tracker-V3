import { hash } from "bcryptjs";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
	const { email, password } = await request.json();

	if (!email || !password) {
		return NextResponse.json(
			{ message: "Email and password are required." },
			{ status: 400 }
		);
	}

	// Hash password with
	//const hashedPassword = await hash(password, 12);

	// Check if user already exists
	//const existingUser = await db.collection("users").findOne({ email });
	const existingUser = null;
	if (existingUser) {
		return NextResponse.json(
			{ message: "User already exists." },
			{ status: 409 }
		);
	}

	// Insert into db

	return NextResponse.json(
		{ message: "User created", userId: "test" },
		{ status: 201 }
	);
}
