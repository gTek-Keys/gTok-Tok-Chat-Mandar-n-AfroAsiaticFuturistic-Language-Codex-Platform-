import { NextPage } from 'next';
import Head from 'next/head';
import LaunchPortal from '../components/LaunchPortal';
import { useRouter } from 'next/router';

const Launch: NextPage = () => {
  const router = useRouter();

  const handleLaunch = () => {
    console.log('Launch initiated from launch page');
    // You can add additional launch logic here
    // For example, redirecting to a chat interface or dashboard
    // router.push('/chat');
  };

  return (
    <>
      <Head>
        <title>Launch Portal - gTok-Tok Codex Platform</title>
        <meta name="description" content="Launch your gTok-Tok Codex experience" />
      </Head>

      <LaunchPortal />
    </>
  );
};

export default Launch;
