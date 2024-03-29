import { ChakraProvider } from "@chakra-ui/react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Aprenda from "./pages/Aprenda";
import Contato from "./pages/Contato";
import CursoIntro from "./pages/CursoIntro";
import Introducao from "./pages/curso/Introducao";
import Bitcoin from "./pages/curso/Bitcoin";
import Blockchain from "./pages/curso/Blockchain";
import CryptoAssets from "./pages/curso/CryptoAssets";
import Chains from "./pages/curso/Chains";
import Tecnologia from "./pages/curso/Tecnologia";
import Parcerias from "./pages/Parcerias";
import Areas from "./pages/Areas";
import MembrosAtuais from "./pages/MembrosAtuais";
import Fundo from "./pages/Fundo";
import Projetos from "./pages/Projetos";
import ProcessoSeletivo from "./pages/ProcessoSeletivo";
import MembrosAlumni from "./pages/MembrosAlumni";

function App() {
  return (
    <ChakraProvider>
      <Navbar />
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/learn" exact element={<Aprenda />} />
        <Route path="/learn/curso-intro" exact element={<CursoIntro />} />
        <Route
          path="/learn/curso-intro/introducao"
          exact
          element={<Introducao />}
        />
        <Route path="/learn/curso-intro/bitcoin" exact element={<Bitcoin />} />
        <Route
          path="/learn/curso-intro/blockchain"
          exact
          element={<Blockchain />}
        />
        <Route
          path="/learn/curso-intro/crypto-assets"
          exact
          element={<CryptoAssets />}
        />
        <Route path="/learn/curso-intro/chains" exact element={<Chains />} />
        <Route
          path="/learn/curso-intro/tecnologia"
          exact
          element={<Tecnologia />}
        />
        <Route path="/contact" exact element={<Contato />} />
        <Route path="/partnerships" exact element={<Parcerias />} />
        <Route path="/areas" exact element={<Areas />} />
        <Route path="/members/actual" exact element={<MembrosAtuais />} />
        <Route path="/members/alumni" exact element={<MembrosAlumni />} />
        <Route path="/fund" exact element={<Fundo />} />
        <Route path="/projects" exact element={<Projetos />} />
        <Route path="/ps" exact element={<ProcessoSeletivo />} />
      </Routes>
      <Footer />
    </ChakraProvider>
  );
}

export default App;
