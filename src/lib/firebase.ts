import {initializeApp,getApps} from "firebase/app";
import {getAuth} from "firebase/auth";
import {getFirestore} from "firebase/firestore";
const config={
 apiKey:process.env.NEXT_PUBLIC_FIREBASE_API_KEY,authDomain:process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
 projectId:process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,storageBucket:process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
 messagingSenderId:process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,appId:process.env.NEXT_PUBLIC_FIREBASE_APP_ID
};
export const firebaseConfigured=()=>Boolean(config.apiKey&&config.authDomain&&config.projectId&&config.appId);
function app(){if(!firebaseConfigured())throw new Error("Firebase is not configured. Set .env.local first.");return getApps().length?getApps()[0]:initializeApp(config);}
export const getFirebaseAuth=()=>getAuth(app());
export const getPortfolioDb=()=>getFirestore(app());