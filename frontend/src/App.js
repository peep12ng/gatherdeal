import logo from './logo.svg';
import './App.css';

function App() {
  return(
  <div className="flex flex-col">
    <div className="overflow-x-auto sm:mx-0.5 lg:mx-0.5">
      <div className="py-2 inline-block min-w-full sm:px-6 lg:px-8">
        <div className="overflow-hidden">
          <table className="min-w-full">
            <thead className="bg-gray-200 border-b">
            <tr>
              <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                번호
              </th>
              <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                이름
              </th>
              <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                쇼핑몰
              </th>
              <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                가격
              </th>
              <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                카테고리
              </th>
            </tr>
            </thead>
            <tbody>
            <tr className="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">1</td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ASUS TUF Gaming B760M-PLUS WIFI 인텍앤컴퍼니
              </td>
              <td>

              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ￦ 208,717
              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                PC/하드웨어
              </td>
            </tr>
            <tr className="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">2</td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                [11번가] ASUS ROG 제피러스듀오 16 GX650RW-L O108W 노트북
              </td>
              <td>

              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ￦ 1,761,510
              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                노트북/모바일
              </td>
            </tr>
            <tr className="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">2</td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                [SSG]MSI M360 박격포 수냉쿨러 (후기이벤트 3만증정)
              </td>
              <td>

              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ￦ 82,650
              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                PC/하드웨어
              </td>
            </tr>
            <tr className="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">2</td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                [하이마트] 포칼 베티스 헤드폰
              </td>
              <td>

              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ￦ 759,050
              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                가전/TV
              </td>
            </tr>
            <tr className="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">2</td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                [위메프] NZXT N7 B650E MATTE WHITE
              </td>
              <td>

              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                ￦ 444,000
              </td>
              <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                PC/하드웨어
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

);
}

export default App;
