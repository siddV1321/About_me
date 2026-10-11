# Siddharth Verma — Student & Researcher Portfolio

Responsive dark-premium portfolio built with Next.js, Tailwind CSS, Firebase Authentication, and Cloud Firestore.

## Features
- Intro, academics, skills, and editable project cards.
- Type `1321` on the public page (not while focused in an input) to reveal admin sign-in.
- Admin label `siddV`; portfolio content editor supports profile, academic data, skills, and project CRUD.
- Firestore writes are restricted by database security rules to one verified admin email.

## Security
The keyboard sequence is only a hidden convenience, not authentication. Anyone can inspect client-side code. Firebase Authentication and Firestore rules are the actual security boundary. `siddV` maps to the one configured Firebase admin email. The requested password `1321` is not hardcoded: it is too short for Firebase Email/Password authentication (minimum 6 characters). Set a strong unique password for the Firebase account. Never place passwords or service-account keys in frontend code.

## Setup
1. Install Node.js 20.9+ (Node 22 LTS recommended).
2. Run `npm install`.
3. Copy `.env.example` to `.env.local` and fill in the web-app config from Firebase Console.
4. In Firebase Console, enable Authentication → Email/Password.
5. Create the one admin user using `NEXT_PUBLIC_ADMIN_EMAIL`; set a strong password and verify the email.
6. Create a Firestore database.
7. Copy `firestore.rules` into Firestore Rules, replace `REPLACE_WITH_ADMIN_EMAIL` with the exact admin email, and publish.
8. Restart the dev server: `npm run dev`.
9. Visit http://localhost:3000, type `1321`, and sign in as `siddV` using the configured admin account password.
10. Run `npm run build` to check production compilation.

Windows PowerShell copy command:
`Copy-Item .env.example .env.local`

## Deploy to Vercel
Push to GitHub, import into Vercel, add all `.env.local` values in Project Settings → Environment Variables, deploy, and verify the Firestore rules use the correct admin email.

Saved content is stored in Firestore document `portfolio/main`. The app uses starter content until that document is saved. Replace placeholder project links and review every claim before public launch. Do not publish your home address, student admission number, or private contact details.
