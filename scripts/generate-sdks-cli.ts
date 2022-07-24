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

const globalConfig = {};

async function main() {
  let CID = "";
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

    for (let i = 0; i < languages.length; i++) {
      const language = languages[i];

      console.log("Creating SDK for: ", chalk.bgGreen(language));
      // openapi-generator-cli generate -i docs/openapi.yaml -g typescript-angular -o generated-sources/openapi --additional-properties=ngVersion=6.1.7,npmName=restClient,supportsES6=true,npmVersion=6.9.0,withInterfaces=true"

      const spawnArguments = [
        path.resolve(
          process.cwd(),
          "./node_modules/@openapitools/openapi-generator-cli"
        ),
        "generate",
        "-i",
        path.resolve(process.cwd(), "openapi.yaml"),
        "-g",
        language,
        "-o",
        `./sdks/${language}`,
        "--skip-validate-spec",
      ];

      const configString = stringifyConfig({
        ...globalConfig,
        ...languageConfig[language],
      });
      if (configString) {
        spawnArguments.push(configString);
      }

      console.log("Spawning pnpx with", spawnArguments);

      const createOutput = spawnSync("pnpx", spawnArguments);

      console.log("Output from create:", createOutput.output.toString());

      // console.log("Unzipping file");
      // spawnSync(`unzip`, [`downloads/${language}.zip`]);

      // console.log("Moving file directory into sdks folder \n");
      // spawnSync("mv", [`${language}-client`, `./sdks/${language}`]);

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

function stringifyConfig(config: Record<string, any>) {
  return Object.entries(config).reduce(
    (additionalPropertiesString, [key, value]) => {
      let newString = additionalPropertiesString;
      if (!newString) {
        newString = `--additional-properties=${key}=${value}`;
      } else {
        newString += `,${key}=${value}`;
      }
      return newString;
    },
    ""
  );
}

main();
