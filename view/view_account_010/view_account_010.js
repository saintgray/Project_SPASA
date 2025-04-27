import { Service } from './service.js'
import { CommonService } from './common.js'

window.onload = () => {
    CommonService.load();
    Service.load();

}