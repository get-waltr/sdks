import fs from "fs-extra";
import path from "path";
import { spawnSync, execSync } from "child_process";
import axios from "axios";
import yaml from "js-yaml";
import chalk from "chalk";

import stream from "stream";
import { promisify } from "util";
const finished = promisify(stream.finished);

function asyncTimeout(duration: number) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(true);
    }, duration);
  });
}

enum Languages {
  Go = "go",
  PHP = "php",
  Python = "python-legacy",
  Typescript = "typescript-axios",
  Elixir = "elixir",
  Ruby = "ruby",
}

const languages: Languages[] = [
  Languages.Elixir,
  Languages.Go,
  Languages.PHP,
  Languages.Python,
  Languages.Ruby,
  Languages.Typescript,
];

const languageConfig: Record<Languages, Record<string, any>> = {
  [Languages.Elixir]: {},
  [Languages.Go]: {},
  [Languages.PHP]: {},
  [Languages.Python]: {},
  [Languages.Ruby]: {},
  [Languages.Typescript]: {
    npmName: "@gilfold/sdk",
  },
};

async function main() {
  try {
    console.log("Removing old builds");
    fs.removeSync(path.resolve(process.cwd(), "sdks"));
    fs.mkdirSync(path.resolve(process.cwd(), "sdks"));
    fs.removeSync(path.resolve(process.cwd(), "downloads"));
    fs.mkdirSync(path.resolve(process.cwd(), "downloads"));

    console.log("Reading openapi.yaml");
    const yamlSpec = fs.readFileSync(
      path.resolve(process.cwd(), "openapi.yaml"),
      {
        encoding: "utf8",
      }
    );

    console.log("Converting yaml to json");
    const spec = yaml.load(yamlSpec);

    console.log("Waiting for server to boot... \n");
    await asyncTimeout(10000);

    const GEN_IP = "localhost";

    for (let i = 0; i < languages.length; i++) {
      const language = languages[i];

      console.log("Creating SDK for: ", chalk.bgGreen(language));

      const createResponse = await axios.post(
        `http://${GEN_IP}:8888/api/gen/clients/${language}`,
        {
          spec,
          options: {
            foo: "bar",
            gitUserId: "go-gilfold",
            gitHost: "github.com",
            gitRepoId: `sdks/clients/${language}`,
            ...languageConfig[language],
          },
        },
        {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
        }
      );

      const { code } = createResponse.data;

      console.log("Downloading file from server");

      await downloadFile(
        `http://${GEN_IP}:8888/api/gen/download/${code}`,
        path.resolve(process.cwd(), `downloads/${language}.zip`)
      );

      console.log("Unzipping file");
      spawnSync(`unzip`, [`downloads/${language}.zip`]);

      console.log("Moving file directory into clients folder \n");
      spawnSync("mv", [`${language}-client`, `./clients/${language}`]);

      await asyncTimeout(4000);
    }
  } catch (e: any) {
    console.log(chalk.bgRed("Caught error: "), { e });
  }

  process.exit(0);
}

// from: https://stackoverflow.com/a/61269447
export async function downloadFile(
  fileUrl: string,
  outputLocationPath: string
): Promise<any> {
  const writer = fs.createWriteStream(outputLocationPath);
  return axios
    .get(fileUrl, {
      responseType: "stream",
    })
    .then((response) => {
      response.data.pipe(writer);
      return finished(writer); //this is a Promise
    });
}

main();
