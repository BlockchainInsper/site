import Materiais from '../../components/curso-intro/Materiais';
import Videos from '../../components/curso-intro/Videos';

const materiais1 = [
  {
    nome: "Symmetric vs Asymmetric encryption",
    link: "https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences"
  }
]

const materiais2 = [
  {
    nome: "Explaining public-key cryptography to non-geeks",
    link: "https://medium.com/@vrypan/explaining-public-key-cryptography-to-non-geeks-f0994b3c2d5"
  }
]

const videos2 = [
  {
    link: "https://www.youtube.com/embed/AQDCe585Lnc"
  },
  {
    link: "https://www.youtube.com/embed/GSTiKjnBaes"
  },
  {
    link: "https://www.youtube.com/embed/GSIDS_lvRv4"
  },
  {
    link: "https://www.youtube.com/embed/vsXMMT2CqqE"
  },
  {
    link: "https://www.youtube.com/embed/pgzWxOtk1zg"
  },
  {
    link: "https://www.youtube.com/embed/dut9EnbFym0"
  },
]


const videos3 = [
  {
    link: "https://www.youtube.com/embed/s22eJ1eVLTU"
  },
  {
    link: "https://www.youtube.com/embed/Aq3a-_O2NcI"
  },
]

const materiais4 = [
  {
    nome: "Understanding Bitcoin Market Participants – Vulnerabilities in the Price of Bitcoin Driven by Miners",
    link: "https://www.blockwaresolutions.com/research-and-publications/2020-halving-analysis"
  }
]

const videos4 = [
  {
    link: "https://www.youtube.com/embed/d4xXJh677J0"
  },
  {
    link: "https://www.youtube.com/embed/L-Qhv8kLESY"
  },
]

const materiais5 = [
  {
    nome: "Why is Diffie-Hellman considered in the context of public key cryptography?",
    link: "https://crypto.stackexchange.com/questions/6307/why-is-diffie-hellman-considered-in-the-context-of-public-key-cryptography"
  }
]

const videos5 = [
  {
    link: "https://www.youtube.com/embed/NmM9HA2MQGI"
  },
  {
    link: "https://www.youtube.com/embed/Yjrfm_oRO0w"
  },
]

const materiais6 = [
  {
    nome: "Cryptographic Hash Function",
    link: "https://www.lifewire.com/cryptographic-hash-function-2625832"
  }
]

const videos6 = [
  {
    link: "https://www.youtube.com/embed/DMtFhACPnTY"
  },
  {
    link: "https://www.youtube.com/embed/b4b8ktEV4Bg"
  },
  {
    link: "https://www.youtube.com/embed/S9JGmA5_unY"
  },
  {
    link: "https://www.youtube.com/embed/8ZtInClXe1Q"
  },
  {
    link: "https://www.youtube.com/embed/0WiTaBI82Mc"
  }
]

const videos7 = [
  {
    link: "https://www.youtube.com/embed/JD72Ry60eP4"
  },
]

const materiais8 = [
  {
    nome: "What is the math behind elliptic curve cryptography?",
    link: "https://hackernoon.com/what-is-the-math-behind-elliptic-curve-cryptography-f61b25253da3"
  }
]

const videos8 = [
  {
    link: "https://www.youtube.com/embed/NF1pwjL9-DE"
  },
  {
    link: "https://www.youtube.com/embed/nybVFJVXbww"
  },
  {
    link: "https://www.youtube.com/embed/dCvB-mhkT0w"
  }
]

const videos9 = [
  {
    link: "https://www.youtube.com/embed/O4xNJsjtN6E"
  },
]

const materiais10 = [
  {
    nome: "Myths about /dev/urandom",
    link: "https://www.2uo.de/myths-about-urandom/"
  }
]

const videos10 = [
  {
    link: "https://www.youtube.com/embed/SxP30euw3-0"
  },
  {
    link: "https://www.youtube.com/embed/LDPMpc-ENqY"
  },
]

const materiais11 = [
  {
    nome: "O efeito da supremacia quântica no futuro da criptografia",
    link: "https://medium.com/brunoartc/o-efeito-da-supremacia-qu%C3%A2ntica-no-futuro-da-criptografia-cd00dc049d5b"
  }
]

const videos11 = [
  {
    link: "https://www.youtube.com/embed/MjwXDuuMW0s"
  },
  {
    link: "https://www.youtube.com/embed/hbiKHELmzuc"
  },
]

const videos12 = [
  {
    link: "https://www.youtube.com/embed/MVPvrGbBKF8"
  },
]

export default function Tecnologia() {
  return (
    <>
      <Materiais materiais={materiais1} titulo="Criptografia simétrica" />

      <Materiais materiais={materiais2} titulo="Criptografia assimétrica" />
      <Videos videos={videos2} titulo="Criptografia assimétrica: Vídeos" />

      <Videos videos={videos3} titulo="Assinaturas Digitais: Vídeos" />

      <Materiais materiais={materiais4} titulo="Consenso" />
      <Videos videos={videos4} titulo="Consenso: Vídeos" />

      <Materiais materiais={materiais5} titulo="Diffie-Hellman" />
      <Videos videos={videos5} titulo="Diffie-Hellman: Vídeos" />

      <Materiais materiais={materiais6} titulo="Hash functions" />
      <Videos videos={videos6} titulo="Hash functions: Vídeos" />

      <Videos videos={videos7} titulo="RSA: Vídeos" />

      <Materiais materiais={materiais8} titulo="Curvas elípticas (ECC)" />
      <Videos videos={videos8} titulo="Curvas elípticas (ECC): Vídeos" />

      <Videos videos={videos9} titulo="AES: Vídeos" />

      <Materiais materiais={materiais10} titulo="Pseudo-random / random" />
      <Videos videos={videos10} titulo="Pseudo-random / random: Vídeos" />

      <Materiais materiais={materiais11} titulo="Criptografia Quântica" />
      <Videos videos={videos11} titulo="Criptografia Quântica: Vídeos" />

      <Videos videos={videos12} titulo="Aula Tech Blockchain Insper 2020.2" />
    </>
  )
}