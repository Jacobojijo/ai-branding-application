import type { NextPage } from "next";
import Head from "next/head";
import CopyKitt from "../components/copykitt";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Brand snippet generator</title>
        <meta
          name="description"
          content="Generate branding snippets for your product."
        />
        <link rel="icon" href="/brand.jpg" />
      </Head>

      <CopyKitt />
    </div>
  );
};

export default Home;
